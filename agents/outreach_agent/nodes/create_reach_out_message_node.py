from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langgraph.types import Command

from agents.outreach_agent.dto.reach_out_message_output import ReachOutMessage
from agents.outreach_agent.prompts.create_reach_out_message_prompt import prompt, prompt_after_validation
from agents.outreach_agent.states.state import State
from constants.ai_models import LLM

llm = LLM(temperature=0.0, stream=False)


async def create_reach_out_message(state: State) -> Command[Literal["reflection"]]:

    # if the message didn't pass the validation
    if state.validation is not None:
        message_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompt_after_validation),
                (
                    "human",
                    "Here is the user info: {user_info}, Here is the initial message: {initial_message}, Here is the feedback: {feedback}",
                ),
            ]
        )

        # I like to use structured output to reinforce correct output format with description
        message_writer = message_prompt | llm.with_structured_output(ReachOutMessage)
        message = message_writer.invoke({"user_info": state.user_info, "initial_message": state.reach_out_message, "feedback": state.validation.reason})

    #if the message didn't go through the validation yet. (initial invoke)
    else:
        message_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompt),
                (
                    "human",
                    "Here is the user info: {user_info}",
                ),
            ]
        )

        # I like to use structured output to reinforce correct output format with description
        message_writer = message_prompt | llm.with_structured_output(ReachOutMessage)
        message = message_writer.invoke({"user_info": state.user_info})

    return Command(goto="reflection", update={"reach_out_message": message})
