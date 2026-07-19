import json
import os

import chromadb
from chromadb.utils import embedding_functions

from src.config import CHROMA_PATH, DATA_PATH

embedding_function = embedding_functions.DefaultEmbeddingFunction()


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name="sports_collection",
        embedding_function=embedding_function
    )

    return collection


def initialize_database():

    collection = get_collection()

    if collection.count() > 0:
        return

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError("sports_facts.json not found")

    with open(DATA_PATH, "r", encoding="utf-8") as file:
        facts = json.load(file)

    documents = []
    ids = []
    metadatas = []

    for index, item in enumerate(facts):

        documents.append(item["fact"])

        ids.append(f"fact_{index}")

        metadatas.append(
            {
                "sport": item["sport"]
            }
        )

    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    print("Database Initialized Successfully")


def retrieve_context(sport):

    collection = get_collection()

    result = collection.query(

        query_texts=[
            f"{sport} history world cup records championships"
        ],

        n_results=5,

        where={
            "sport": sport
        }

    )

    documents = result["documents"][0]

    return "\n".join(documents)