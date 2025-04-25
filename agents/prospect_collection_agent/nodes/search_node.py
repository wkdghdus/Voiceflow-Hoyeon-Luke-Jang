from tavily import TavilyClient

from agents.prospect_collection_agent.states.state import State


def linkedin_search(state:State):
    search = TavilyClient()
    response = search.search(query=state.queries[2], max_results=10, search_depth="advanced", include_domains=["linkedin.com"], include_answer=True)

    return {"results": response["results"], "answer": [response["answer"]]}

def google_search(state:State):
    search = TavilyClient()
    response = search.search(query=state.queries[0], max_results=10, search_depth="advanced", include_domains=["google.com"], include_answer=True)

    return {"results": response["results"], "answer": [response["answer"]]}

def twitter_search(state:State):
    search = TavilyClient()
    response = search.search(query=state.queries[1], max_results=10, search_depth="advanced", include_domains=["x.com"], include_answer=True)

    return {"results": response["results"], "answer": [response["answer"]]}

