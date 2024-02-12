# importing required libraries
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# path to your data (the medicine book you want your model to retrieve information from)
data_path = 'medicine_book.pdf'

# path for storing vectors locally on machine (word embeddings)
vector_store_path = 'vectors'


# creating vector database for medicine book
def create_vectors():
    # creating loader object with file path
    loader = PyPDFLoader(data_path)

    # loading the contents of the pdf file
    documents = loader.load()

    # splitting the pdf text to small chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents=documents)

    # creating embeddings for the text using Hugging Face embeddings (384 dimensions)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device': 'cpu'})

    # using FAISS for storing embeddings
    db = FAISS.from_documents(chunks, embeddings)

    # saving n local machine for faster retrieval
    db.save_local(vector_store_path)


if __name__ == '__main__':
    create_vectors()
