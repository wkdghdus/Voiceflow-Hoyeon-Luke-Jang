from typing import Literal
from langgraph.types import Command

from constants.ai_models import LLM
from agents.reply_agent.states.state import State

# initialize llm based on presets
# practice to change llm models in an ease
llm = LLM(temperature=0.0, stream=False)

def _new_response_available():
    """
    method that checks if there is a new response
    :return: True if there is a new response, False if not
    """

    return True

def check_response(state: State) -> Command[Literal["create_reply", "__end__"]]:
    """
    checks if there are any new data in which prospect_collection_agent appended

    :param state: state of the agent
    :return: Command to next node. End if there is no new data, creates reach out messages if there is.
    """

    if _new_response_available():
        messages = [{"Human": "placeholder"}]
        ### logic to update messages
        return Command(goto="create_reply", update={"messages": messages})

    return Command(goto="__end__")