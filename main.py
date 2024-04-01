import streamlit as st
import streamlit.components.v1 as components
from rag_model import RAGModel  # Import the RAGModel class
from langchain_community.document_loaders import PyPDFLoader


from PyPDF2 import PdfReader
from langchain.docstore.document import Document

def main():
    st.title("🌚 RAG System Page (draft)")
    st.write("What do you want to know? (you can add more evident about them, like PDF, their website)")
    
    form_text = st.text_area(label="What's your question")
    upload_file = st.file_uploader("upload PDF/text file (optional)", 
                                #    accept_multiple_files=True, 
                                   type=['pdf','txt'], )
    form_url = st.text_input("url (optional)")
    
    if st.button("Submit", type="primary"):
        print(form_text)
        print(upload_file)
        print(form_url)
        with st.spinner('generating answer'):
            rag_model = RAGModel(model_name='SeaLLM')
            if form_url:
                print('get data from webpage')
                res = rag_model.get_webdata(url=form_url, prompt=form_text)
                res = res['result']
            elif upload_file:
                print('get data from text file')
                docs = process_uploaded_file(upload_file)
                res = rag_model.get_upload_file_data(docs, prompt=form_text)
                
            else:
                print('generate simple answer')
                res = rag_model.prompt_simple(form_text)

            st.write(res)



            
def process_uploaded_file(uploaded_file) -> Document:
    file_type = uploaded_file.name.split('.')[-1]
    match file_type:
        case 'pdf':
            docs = []
            reader = PdfReader(uploaded_file)
            i = 1
            for page in reader.pages:
                docs.append(Document(page_content=page.extract_text(), metadata={'page':i}))
                i += 1
        case 'txt':
            file_content = uploaded_file.getvalue().decode("utf-8")
            docs = [Document(page_content=file_content, metadata={'page': 1})]
        
    return docs
        


if __name__ == '__main__':
    
    main()
