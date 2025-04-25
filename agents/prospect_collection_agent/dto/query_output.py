from pydantic import BaseModel, Field

class Queries(BaseModel):
    linkedin_query: str = Field(description="query for LinkedIn")
    google_query: str = Field(description="query for Google")
    twitter_query: str = Field(description="query for Twitter")
