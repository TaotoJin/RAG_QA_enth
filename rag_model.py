from langchain.llms import Ollama
from langchain.vectorstores import Chroma

# from langchain_community.llms import Ollama
# from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

from langchain import PromptTemplate

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
# from langchain_community.embeddings import OllamaEmbeddings
# from chromadb.utils import embedding_functions
# default_ef = embedding_functions.DefaultEmbeddingFunction()

# from langchain.document_loaders import WebBaseLoader, TextLoader, PyPDFLoader
from langchain.docstore.document import Document
from langchain_community.document_loaders import WebBaseLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain


class RAGModel:

    def __init__(self, model_name:str,):
         
        self.llm = Ollama(model=model_name)
        self.embedding = FastEmbedEmbeddings()

        self.text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        self.db_dir = './chroma_db/'
        self.vector_db = self.load_db()
    

    def load_db(self):
        vector_db = Chroma(persist_directory=self.db_dir, 
                                embedding_function=self.embedding)
        vector_db.persist()
        

    def get_webdata(self, url:str, prompt:str):
        loader = WebBaseLoader(url)
        data = loader.load()
        docs = self.text_splitter.split_documents(data)

        # ? should i add webdata into db
        data = loader.load()
        res = self.find_ans_from_context(data, prompt)
        return res


    def get_textfile_data(self, file_path:str, prompt:str):

        file_type = file_path.split('.')[-1]
        if file_type == 'txt':
            loader = TextLoader(file_path, encoding='utf8')
        elif file_type == 'pdf':
            loader = PyPDFLoader(file_path)

        data = loader.load()
        res = self.find_ans_from_context(data, prompt)
        return res['result']
    
    def get_upload_file_data(self, docs: Document, prompt:str):
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        data = text_splitter.split_documents(docs)
        res = self.find_ans_from_context(data, prompt)
        return res['result']

    def prompt_simple(self, prompt:str,):
        res = self.llm(prompt)
        return res

    def find_ans_from_context(self, data, prompt:str):
        
        docs = self.text_splitter.split_documents(data)

        vectordb = Chroma.from_documents(documents=docs, 
                                        embedding=self.embedding,
                                        persist_directory=self.db_dir)
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})
        qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever)
        res = qa(prompt)
        return res





# if __name__ == '__main__':
    # LLM_MODEL = 'SeaLLM'
    # rag_model = RAGModel(model_name=LLM_MODEL)


    # print("# test simple prompt")
    # print(rag_model.prompt_simple(input()), end='\n\n')

#     # test prompt with context

    # print('# test qa with website')
    # print(rag_model.get_webdata('https://th.wikipedia.org/wiki/%E0%B8%A1%E0%B8%93%E0%B8%91%E0%B8%A5%E0%B8%9D%E0%B8%B9%E0%B9%80%E0%B8%88%E0%B8%B5%E0%B9%89%E0%B8%A2%E0%B8%99', prompt='ฟูเจี้ยนอยู่ติดกับเมืองอะไร'), end='\n\n')

    # print('# test qa with textfile')
    # print(rag_model.get_textfile_data('./LLM/file/sayaka.txt', prompt='who is sayaka'), end='\n\n')

#     print('# test qa with pdf')
#     print(rag_model.get_textfile_data('./ref/README.pdf', prompt='how to install ollama'), end='\n\n')

        