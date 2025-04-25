"""Define a data enrichment agent.

Works with a chat model with tool calling support.
"""

from langgraph.graph import END, START
from langgraph.graph import StateGraph

from agents.prospect_collection_agent.edges.wait_for_three_inputs_edge import wait_for_three_inputs
from agents.prospect_collection_agent.nodes.append_to_db_node import append_to_db
from agents.prospect_collection_agent.nodes.create_query_node import create_query
from agents.prospect_collection_agent.nodes.search_node import linkedin_search, google_search, twitter_search
from agents.prospect_collection_agent.states.state import State

# Create the graph
workflow = StateGraph(State,)

workflow.add_node("create_query", create_query)
workflow.add_node("search_linkedin", linkedin_search)
workflow.add_node("search_google", google_search)
workflow.add_node("search_twitter", twitter_search)
workflow.add_node("append_to_db", append_to_db)
workflow.add_node("wait", wait_for_three_inputs)

workflow.add_edge(START, "create_query")
workflow.add_edge("create_query", "search_linkedin")
workflow.add_edge("create_query", "search_google")
workflow.add_edge("create_query", "search_twitter")
workflow.add_edge("search_linkedin", "wait")
workflow.add_edge("search_google", "wait")
workflow.add_edge("search_twitter", "wait")
# wait -> append_to_db is dealt using Command due to convenience.
workflow.add_edge("append_to_db", END)

graph = workflow.compile()
