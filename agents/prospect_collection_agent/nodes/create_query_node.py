from langchain_core.prompts import ChatPromptTemplate

from agents.prospect_collection_agent.dto.query_output import Queries
from agents.prospect_collection_agent.prompts.create_query_prompt import prompt
from constants.ai_models import LLM
from agents.prospect_collection_agent.states.state import State

llm = LLM(temperature=0.0, stream=False)


def create_query(state: State):
    query_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", prompt),
        ]
    )

    # Re-write query
    query_writer = query_prompt | llm.with_structured_output(Queries)
    queries = query_writer.invoke({})

    # update state
    return {"linkedin_query": queries.linkedin_query,
            "google_query": queries.google_query,
            "twitter_query": queries.twitter_query}
