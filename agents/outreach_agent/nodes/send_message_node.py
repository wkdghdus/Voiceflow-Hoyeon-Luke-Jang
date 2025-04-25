from typing import Literal

from langgraph.types import Command

from agents.outreach_agent.states.state import State


def send_message(state:State) -> Command[Literal["update_db"]]:
    #logic to send message

    return Command(goto="__end__")
