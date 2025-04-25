"""Define a data enrichment agent.

Works with a chat model with tool calling support.
"""

from langgraph.graph import END, START
from langgraph.graph import StateGraph

from agents.reply_agent.nodes.check_response import check_response
from agents.reply_agent.nodes.create_reply_node import create_reply
from agents.reply_agent.nodes.reflection_node import reflection
from agents.reply_agent.nodes.send_message_node import send_message
from agents.reply_agent.states.state import State

# Create the graph
workflow = StateGraph(State)

# add nodes
workflow.add_node("check_response", check_response)
workflow.add_node("create_reply", create_reply)
workflow.add_node("reflection", reflection)
workflow.add_node("send_message", send_message)

# no edge needed since it is already dealt with Command (except start)
workflow.add_edge(START, "check_response")

graph = workflow.compile()
