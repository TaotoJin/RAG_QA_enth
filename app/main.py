import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title("🌚 RAG System Page (draft)")
    st.write("What do you want to know about this guy ? (you can add more evident about them, like PDF, their website)")

    form_text = st.text_area(label="What's your question")
    st.file_uploader("upload PDF/text file (optional)",     accept_multiple_files=True, type=['pdf','txt'])
    form_url = st.text_input("url (optional)")
    
    if st.button("Submit", type="primary"):
        st.write("You question was sent")
        st.text("please wait for future implementation, soon")
        st.markdown("![gif](https://media1.tenor.com/m/GIYnmPBTFsUAAAAC/keyboard-anime.gif)")


if __name__ == '__main__':
    main()