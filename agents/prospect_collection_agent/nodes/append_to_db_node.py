from typing import Literal

from langgraph.types import Command

from agents.outreach_agent.states.state import State


def append_to_db(state: State) -> Command[Literal["__end__"]]:
    # logic to update DB with certain flag telling that message has been sent to someone.

    return Command(goto="__end__")

