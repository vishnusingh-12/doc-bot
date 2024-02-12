# !!! For GPU llama cpp needs some additional steps for installation. Check the below link for reference.
# https://python.langchain.com/docs/integrations/llms/llamacpp

# importing required libraries
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import chainlit as cl
from langchain_community.llms import LlamaCpp

# path where vectors are stored
vector_store_path = 'vectors'


def load_llm():
    """
    Loads the llm using LlamaCpp and returns the llm.
    """
    print("loading llm")
    llm = LlamaCpp(
        # path to your local llama2 model
        model_path='D:\ML Resources\Projects\Langchain\chatbot\llama-2-7b-chat.Q8_0.gguf',

        # maximum number of tokens (input + output) that the model can generate
        max_tokens=1024,

        # number of gpu layers to be used, -1 for all layers, avoid in case of cpu loading
        n_gpu_layers=-1,

        # allows the model to offload the computation of key, query, and value vectors for certain layers
        offload_kqv=True,

        # the number of tokens the model can take as input at a time
        n_batch=256,

        # maximum tokens(input + output) that the model can process in one go. Max is 4096
        n_ctx=2048,

        # print the details of the execution of the llm
        verbose=True,

        # set for sampling tokens. High temp means less predictable output
        temperature=0.5
    )
    print('llm loaded')
    return llm


# loading llm before running chainlit app as it will be required throughout the program
llm = load_llm()

# creating embeddings for the text using Hugging Face embeddings (384 dimensions)
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                   model_kwargs={'device': 'cpu'})

# loading the locally stored vectors
db = FAISS.load_local(vector_store_path, embeddings)


def retrieval_qa_chain():
    """
    Creates and returns a Retrieval qa chain
    :return: Retrieval qa chain
    """

    # retriever uses the vector store(db) to retrieve documents that we fed
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type='stuff',
                                           retriever=db.as_retriever(search_kwargs={'k': 2}),
                                           return_source_documents=True)
    return qa_chain


# chainlit

# decorator showing start() function will be called when chat starts
@cl.on_chat_start
async def start():
    # creating chain
    chain = retrieval_qa_chain()

    # sends an opening message
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome to Medical Bot. What is your query?"
    await msg.update()

    # setting session variable
    cl.user_session.set("chain", chain)


@cl.on_message
async def main(message: cl.Message):

    # getting the session variable chain
    chain = cl.user_session.get("chain")

    # creating a callback handler
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True

    # getting result from chain
    res = await chain.acall({'query': message.content}, callbacks=[cb])

    # getting answer from chain output
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        pass
    else:
        answer += "\nNo sources found"
