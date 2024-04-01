import streamlit as st
import streamlit.components.v1 as components
from rag_model import RAGModel  # Import the RAGModel class




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
            else:
                print('generate simple answer')
                res = rag_model.prompt_simple(form_text)

            st.write(res)

        



if __name__ == '__main__':
    
    main()
