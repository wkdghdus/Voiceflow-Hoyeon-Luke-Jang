from pydantic import BaseModel, Field

class ReachOutMessage(BaseModel):
    message: str = Field(description="""The output will be a concise, personalized outreach message tailored specifically to the provided user information. 
                                        The message will clearly highlight relevant Voiceflow features, establish a friendly connection with the user, 
                                        and conclude with an inviting call-to-action.""")

