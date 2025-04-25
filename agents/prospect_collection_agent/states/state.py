"""State definitions.

State is the interface between the graph and end user as well as the
data model used internally by the graph.
"""

from operator import add
from typing import Annotated, Optional

from pydantic import Field, BaseModel


class State(BaseModel):
    linkedin_query: Optional[str] = Field(description="query for LinkedIn")
    google_query: Optional[str] = Field(description="query for Google")
    twitter_query: Optional[str] = Field(description="query for Twitter")
    results: Annotated[list[dict], add] = Field(default=None)
    answer: Annotated[list[str], add] = Field(default="")
