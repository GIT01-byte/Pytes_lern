from typing import Optional
from pydantic import BaseModel, Field


class ProgrammRead(BaseModel):
    id: Optional[int]
    title: str
    author: str 
    description: Optional[str]

    model_config = {
        "from_attributes": True
    }


class ProgrammAdd(BaseModel):
    id: Optional[int] = Field(default=1)
    title: str = Field(default='N/A')
    author: str = Field(default='N/A')
    description: Optional[str] = Field(default='N/A')
    license_key: int = Field(ge=10, le=10)
