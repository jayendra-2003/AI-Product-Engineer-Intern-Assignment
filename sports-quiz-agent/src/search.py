from duckduckgo_search import DDGS


def get_live_news(sport):

    query = f"{sport} latest tournament winner recent sports news"

    context = []

    try:

        with DDGS() as ddgs:

            results = ddgs.text(query, max_results=5)

            for result in results:

                title = result.get("title", "")

                body = result.get("body", "")

                context.append(f"{title}\n{body}")

    except Exception as e:

        print(e)

        return "No recent news available."

    return "\n\n".join(context)