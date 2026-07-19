import os

from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from config import (
    OPENAI_API_KEY,
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K_RESULTS
)

load_dotenv()

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


embeddings = OpenAIEmbeddings(
    model=EMBEDDING_MODEL
)

vectorstore = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": TOP_K_RESULTS}
)


def retrieve_context(query, k=TOP_K_RESULTS):

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context