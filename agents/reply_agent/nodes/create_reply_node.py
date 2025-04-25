from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langgraph.types import Command

from agents.reply_agent.dto.reply_output import Reply
from agents.reply_agent.prompts.create_reply_prompt import prompt, prompt_after_validation
from agents.reply_agent.states.state import State
from constants.ai_models import LLM

llm = LLM(temperature=0.0, stream=False)


async def create_reply(state: State) -> Command[Literal["reflection"]]:

    # if the message didn't pass the validation
    if state.validation is not None:
        message_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", prompt_after_validation),
                ("placeholder","{messages}"),
                (
                    "human",
                    "Here is the user info: {user_info}, Here is the initial reply: {initial_reply}, Here is the feedback: {feedback}",
                ),
            ]
        )

        # I like to use structured output to reinforce correct output format with description
        message_writer = message_prompt | llm.with_structured_output(Reply)
        message = message_writer.invoke({"user_info": state.user_info, "initial_reply": state.reply, "feedback": state.validation.reason})

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
        message_writer = message_prompt | llm.with_structured_output(Reply)
        message = message_writer.invoke({"user_info": state.user_info})

    return Command(goto="reflection", update={"reply": message})
