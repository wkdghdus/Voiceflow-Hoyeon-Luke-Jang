"""Define a data enrichment agent.

Works with a chat model with tool calling support.
"""

from langgraph.graph import START
from langgraph.graph import StateGraph

from agents.outreach_agent.nodes.check_new_data_node import check_new_data
from agents.outreach_agent.nodes.create_reach_out_message_node import create_reach_out_message
from agents.outreach_agent.nodes.reflection_node import reflection
from agents.outreach_agent.nodes.send_message_node import send_message
from agents.outreach_agent.nodes.update_db_node import update_db
from agents.outreach_agent.states.state import State

# Create the graph
workflow = StateGraph(State)

# add nodes
workflow.add_node("check_new_data", check_new_data)
workflow.add_node("create_reach_out_message", create_reach_out_message)
workflow.add_node("reflection", reflection)
workflow.add_node("send_message", send_message)
workflow.add_node("update_db", update_db)

# no edge needed since it is already dealt with Command (except Start)
workflow.add_edge(START, "check_new_data")


graph = workflow.compile()
