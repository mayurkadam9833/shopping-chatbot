from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import Chroma 
from src.helper import load_url_data,text_splitter,download_embeddings
from src.webscraping import product_links



extracted_data=load_url_data(product_links)
text_chunk=text_splitter(extracted_data)
embeddings=download_embeddings()



dir="vector_database" 

vector_data=Chroma.from_documents(
    documents=text_chunk,
    persist_directory=dir,
    embedding=embeddings
)