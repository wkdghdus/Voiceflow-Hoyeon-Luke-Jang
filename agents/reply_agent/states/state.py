from operator import add
from typing import Annotated, List, Optional
from pydantic import Field, BaseModel

from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class State(BaseModel):
    messages: Annotated[List[BaseMessage], add_messages] = Field(default_factory=list)
    reply: Optional[str] = Field(default=None)
    user_info: Optional[dict] = Field(default=None)
    initial_data: Optional[str] = Field(default=None)
    validation: Optional[BaseModel] = Field(default=None)