import os

from dotenv import load_dotenv
from tavily import TavilyClient

from config import (
    TAVILY_API_KEY,
    MAX_WEB_RESULTS
)

load_dotenv()

client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query):

    try:

        results = client.search(
            query=query,
            max_results=MAX_WEB_RESULTS
        )

        context = ""

        for result in results["results"]:

            context += (
                f"Title: {result['title']}\n"
                f"Content: {result['content']}\n"
                f"Source: {result['url']}\n\n"
            )

        return context

    except Exception as e:

        return f"Web search failed: {str(e)}"