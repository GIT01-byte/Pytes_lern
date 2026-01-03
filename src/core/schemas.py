from typing import Optional
from pydantic import BaseModel, Field


class ProgrammRead(BaseModel):
    id: int
    title: str
    author: str 
    description: str

    model_config = {
        "from_attributes": True
    }


class ProgrammAdd(BaseModel):
    id: Optional[int] = Field(default=1)
    title: str = Field(default='N/A')
    author: str = Field(default='N/A')
    description: Optional[str] = Field(default='N/A')
