# SourceCode Analysis using GenAI(Llama2)

This project implements a chatbot using Retrieval Question Answering (QA) techniques. The chatbot is built using Flask, LangChain, Hugging Face Transformers, and Llama2.

## Overview
The Flask chatbot application is a web-based conversational interface that leverages artificial intelligence (AI) models to interact with users, respond to queries, and provide assistance. It is built using Python and Flask, a lightweight web application framework.

### Installation
1. Clone the repository:
```
git clone https://github.com/deepakthakur-92/SourceCode_Analysis_using_GenAI.git
```

2. Create a virtual environment:

```
conda create -n envname python=3.8 -y
conda activate envname
pip install -r requirements.txt
```

3. Download the quantize model and place it in the model/ directory.
```
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```


## Tools Used
* Flask: Web framework used for building the chatbot interface.
* LangChain: Python library for natural language processing tasks such as document retrieval and question answering.
* Hugging Face Transformers: Library providing pre-trained models and tools for natural language understanding tasks.
* Chromadb: Library for efficient similarity search and clustering of dense vectors.
* GitPython: Library for interacting with Git repositories programmatically, providing functionality for tasks such as repository management, committing changes, and querying repository history.

## Usage
1. Run the Flask app:

```
python app.py
```
2. Access the chatbot interface through your web browser at http://localhost:8080.

3. Enter your questions in the input field and click "Submit" to receive answers from the chatbot.

## Screenshot:

![alt text](image-1.png)