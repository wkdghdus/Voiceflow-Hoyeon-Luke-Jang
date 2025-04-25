from typing import Literal

from langgraph.types import Command

from agents.reply_agent.states.state import State

def send_message(state:State) -> Command[Literal["__end__"]]:

    return Command(goto="__end__", update={"messages": state.reply})
