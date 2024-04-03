
# RAG System

The Retrieve and Generate (RAG) model merges retrieval-based and generative AI to enhance NLP. This documentation outlines the implementation of a bilingual RAG system, supporting both Thai and English


# Demo

[![RAG scheenshot](/file/rag_screenshot.png)](https://youtu.be/f64ZpEWrBPU)
Demo video: [https://youtu.be/f64ZpEWrBPU](https://youtu.be/f64ZpEWrBPU)
# Installation and Setup

## Pre-requisite install Ollama
-  Begin by downloading the Ollama software from the official website. Download link here: [Download Ollama](https://ollama.com/download)

### Download & Install LLM Model on local machine
- For this setup, we will be using the **SEALLM** as the local LLM. SEALLM supports both English and Thai languages. (However, you may consider other LLM e.g. Typhoon or Wangchanglm)
	- SEALLM model is quite large, which may too large for some local machines. So, we're using a quantized version of the model. 
### Steps to Install SEALLM:
1. download the quantized version of SEALLM (gguf file) from the following link:[download SeaLLM gguf here](https://huggingface.co/LoneStriker/SeaLLM-7B-v2-GGUF/blob/main/SeaLLM-7B-v2-Q3_K_L.gguf)
2. Create a `Modelfile` on local machine
3. Edit the `Modelfile` in text editor, like this			
```Modelfile
FROM ./SeaLLM-7B-v2-Q3_K_L.gguf
```
4. Create a model from  `Modelfile` with this command	
```bash
oolama create SeaLLM -f Modelfile
```
5. Run the model 
```bash
ollama run SeaLLM
```
6. check if the model installed successfully, with command `ollama list`, we can see the model name
```console
NAME            ID              SIZE    MODIFIED
SeaLLM:latest   8fe1fd41bb4d    3.9 GB  45 hours ago
```


# Setting up this project


1. Clone this repository

```bash
git clone https://github.com/TaotoJin/RAG_QA_enth.git
```

2. Install dependencies
```bash
pip install -r requiremens.txt
```
3. To use the application, it will open in a web browser, allowing interaction with the RAG system.
```bash
streamlit run main.py
```
