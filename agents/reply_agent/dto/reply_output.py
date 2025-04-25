from pydantic import BaseModel, Field

class Reply(BaseModel):
    message: str = Field(description="The output will be a brief, personalized initial reply designed to promptly acknowledge and address the customer's inquiry or interest about Voiceflow.")

