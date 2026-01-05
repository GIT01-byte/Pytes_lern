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
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        for attr in ["title", "author", "description"]:
            if getattr(self, attr) != getattr(other, attr):
                return False
        return True


class ProgrammAdd(BaseModel):
    id: Optional[int] = Field(default=1)
    title: str = Field(default='N/A')
    author: str = Field(default='N/A')
    description: Optional[str] = Field(default='N/A')
    license_key: str = Field(min_length=10, max_length=10)
