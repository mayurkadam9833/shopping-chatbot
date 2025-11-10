from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def load_url_data(url_list:list): 
    loader=UnstructuredURLLoader(urls=url_list)
    documents=loader.load()
    return documents 

def text_splitter(data): 
    text_split=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=100)
    text_chunk=text_split.split_documents(data)
    return text_chunk 

def download_embeddings(): 
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings