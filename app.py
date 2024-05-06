from langchain.vectorstores import Chroma
from src.helper import load_embedding
from dotenv import load_dotenv
import os
from src.helper import repo_ingestion
from flask import Flask, render_template, jsonify, request
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import CTransformers

app = Flask(__name__)

embeddings = load_embedding()
persist_directory = "db"
# Now we can load the persisted database from disk, and use it as normal.
vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embeddings)

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':128,
                          'temperature':0.01,
                          'context_length': 2000})

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)

qa = ConversationalRetrievalChain.from_llm(llm, 
                                           retriever=vectordb.as_retriever(search_type="mmr", 
                                            search_kwargs={"k":3}), 
                                           memory=memory)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=["GET", "POST"])
def gitRepo():

    if request.method == 'POST':
        user_input = request.form['question']
        repo_ingestion(user_input)
        os.system("python store_index.py")

    return jsonify({"response": str(user_input) })

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)

    if input == "clear":
        os.system("rm -rf repo")

    result = qa(input)
    print(result['answer'])
    return str(result["answer"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
