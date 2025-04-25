from pydantic import BaseModel, Field

class Reflection(BaseModel):
    result: bool = Field(description="True if reach out message is suitable, false if not suitable")
    reason: str = Field(description="Reason of the result in less than 5 sentences")
