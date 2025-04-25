from typing import Literal

from langchain_core.prompts import ChatPromptTemplate
from langgraph.types import Command

from agents.reply_agent.dto.reflection_output import Reflection
from agents.reply_agent.prompts.reflection_prompt import prompt
from agents.reply_agent.states.state import State
from constants.ai_models import LLM

llm = LLM(temperature=0.0)


def reflection(state: State) -> Command[Literal["create_reply", "send_message"]]:

    validation_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
            ("placeholder", "{messages}"),
            ("human", """
                        Here is the user info: {user_info}
                        Here is the corresponding reply: {reply}
                      """)
        ]
    )

    # Re-write query
    validator = validation_prompt | llm.with_structured_output(Reflection)
    validation = validator.invoke({"messages": state.messages,"user_info": state.user_info, "reply": state.reply})

    if validation.result == True:
        return Command(goto="send_message", update={"validation": validation})
    else:
        return Command(goto="create_reply_message", update={"validation": validation})



