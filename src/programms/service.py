from typing import Optional
from .repository import ProgrammsRepo

from core.schemas import ProgrammAdd, ProgrammRead
from core.db import sync_engine


class ProgrammService:
    @classmethod
    def setup_db(cls):
        ProgrammsRepo.create_tables()
    
    @classmethod
    def get_all(cls):
        programms = ProgrammsRepo.get_all_programms()
        return programms

    @classmethod
    def get(cls, programm_id: int):
        programms = ProgrammsRepo.get_programm(programm_id)
        return programms
    
    @classmethod
    def count(cls):
        count = ProgrammsRepo.count_of_programms()
        return count
    
    @classmethod
    def create_programm(cls, programm: ProgrammAdd) -> int:
        new_programm = ProgrammsRepo.add_programm(programm)
        
        return new_programm
    
    @classmethod
    def delete_programm(cls, programm_id: int):
        ProgrammsRepo.delete_programm(programm_id)
     
    @classmethod
    def clear(cls):
        ProgrammsRepo.delete_all()
    
    @classmethod
    def close_db_conection(cls):
        sync_engine.dispose()
    