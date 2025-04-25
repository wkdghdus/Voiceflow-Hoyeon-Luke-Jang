from typing import Optional
from pydantic import Field, BaseModel



class State(BaseModel):
    reach_out_message: Optional[str] = Field(default=None)
    user_info: Optional[dict] = Field(default=None)
    initial_data: Optional[str] = Field(default=None)
    validation: Optional[BaseModel] = Field(default=None)