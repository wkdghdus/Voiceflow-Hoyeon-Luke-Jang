from typing import Literal
from langgraph.types import Command

from agents.prospect_collection_agent.states.state import State


def wait_for_three_inputs(state:State) -> Command[Literal["append_to_db"]]:

    print("-----------------------")
    print(len(state.results))
    print(len(state.answer))

    if len(state.answer) > 2:
        return Command(goto="summarize")
