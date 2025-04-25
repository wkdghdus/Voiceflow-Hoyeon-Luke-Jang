from typing import Literal
from langgraph.types import Command

from constants.ai_models import LLM
from agents.outreach_agent.states.state import State

# initialize llm based on presets
# practice to change llm models in an ease
llm = LLM(temperature=0.0, stream=False)

def _fetch_prospects_data():
    """
    method that fetches prospect data from whatever database
    :return: list of data
    """

    return ["placeholder"]

def check_new_data(state: State) -> Command[Literal["create_reach_out_message", "__end__"]]:
    """
    checks if there are any new data in which prospect_collection_agent appended

    :param state: state of the agent
    :return: Command to next node. End if there is no new data, creates reach out messages if there is.
    """

    current_data = _fetch_prospects_data()

    if state.initial_data != current_data:
        new_data = {"username": "user_infos", "username2": "user_infos2"}
        ### logic to parse and add new data
        return Command(goto="create_reach_out_message", update={"user_info": new_data})

    return Command(goto="__end__")