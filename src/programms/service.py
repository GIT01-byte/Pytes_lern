from typing import Optional
from .repository import ProgrammsRepo

from core.schemas import ProgrammAdd, ProgrammRead
from core.db import async_engine


class ProgrammService:
    @classmethod
    async def get_all(cls):
        programms = await ProgrammsRepo.get_all_programms()
        return programms
    
    @classmethod
    async def count(cls):
        count = await ProgrammsRepo.count_of_programms()
        return count
    
    @classmethod
    async def create_programm(cls, programm: ProgrammAdd) -> int:
        new_programm = await ProgrammsRepo.add_programm(programm)
        
        return new_programm
    
    @classmethod
    async def delete_programm(cls, programm_id: int):
        await ProgrammsRepo.delete_programm(programm_id)
     
    @classmethod
    async def clear(cls):
        await ProgrammsRepo.delete_all()
    
    @classmethod
    async def close_db_conection(cls):
        await async_engine.dispose()
    