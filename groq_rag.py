from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(model_name='openai/gpt-oss-120b')

prompt = ChatPromptTemplate.from_template('''Answer from the dollowing context only. please provide more accurate results based on conext only. {context}
                                   if you dont know the answer directly say i dont know 
                                  Question: {input}  ''')


def generate_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model='nomic-embed-text')
        st.session_state.loader = PyPDFDirectoryLoader("Data")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.splitted = st.session_state.splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.splitted, embedding=st.session_state.embeddings)
        st.write("Vector Database is Ready! ")

st.title("GROQ LPU CHATBOT")

st.write("please click thebutton below to generate embeddings of your data")

if st.button('Generate Embeddings'):
    generate_embedding()


user_input = st.text_input("Enter your query from the uploaded document. ")

if st.button("Answer"):
    if user_input:
        document_context = create_stuff_documents_chain(model, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieved_data = create_retrieval_chain(retriever, document_context)
        response = retrieved_data.invoke({'input':user_input})

        st.write("*** Answer ***")

        st.write(response['answer'])

        with st.expander("Content from the documents: "):
            if "context" in response:
                for i, doc in enumerate(response['context']):
                    st.write(doc.page_content)
                    st.write("---------------------------------")



