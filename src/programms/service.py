from typing import Optional
from .repository import ProgrammsRepo

from core.schemas import ProgrammAdd, ProgrammRead


class ProgrammService:
    @classmethod
    async def get_all(cls):
        programms = await ProgrammsRepo.get_all_programms()
        return programms
    
    @classmethod
    async def create_programm(
        cls, 
        id: Optional[int], 
        title: str, 
        author: str, 
        description: Optional[str]
    ) -> int:
        programm_to_add = ProgrammAdd(
            id=id,
            title=title,
            author=author,
            description=description,
        )
        new_programm = await ProgrammsRepo.add_programm(programm_to_add)
        
        return new_programm
    
    @classmethod
    async def clear(cls):
        await ProgrammsRepo.delete_all()
    
    @classmethod
    async def count(cls):
        count = await ProgrammsRepo.count_of_programms()
        return count
    