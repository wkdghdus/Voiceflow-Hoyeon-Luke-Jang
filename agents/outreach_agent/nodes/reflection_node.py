from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langgraph.types import Command

from agents.outreach_agent.dto.reflection_output import Reflection
from agents.outreach_agent.prompts.reflection_prompt import prompt
from agents.outreach_agent.states.state import State
from constants.ai_models import LLM

llm = LLM(temperature=0.0)


def reflection(state: State) -> Command[Literal["create_reach_out_message", "send_message"]]:

    validation_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("human", """
                        Here is the user info: {user_info}
                        Here is the corresponding reach out message: {reach_out_message}
                      """)
        ]
    )

    # Re-write query
    validator = validation_prompt | llm.with_structured_output(Reflection)
    validation = validator.invoke({"user_info": state.user_info, "reach_out_message": state.reach_out_message})

    if validation.result == True:
        return Command(goto="send_message", update={"validation": validation})
    else:
        return Command(goto="create_reach_out_message", update={"validation": validation})



