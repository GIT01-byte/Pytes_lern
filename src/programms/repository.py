from sqlalchemy import and_, select

from core.db import Base, async_engine, async_session_factory

from core.models import Programm
from core.schemas import ProgrammRead, ProgrammAdd


class ProgrammsRepo:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def get_all_programms():
        async with async_session_factory() as session:
            query = select(Programm)
            res = await session.execute(query)
            result_orm = res.scalars().all()
            print(f"{result_orm=}")

            result_dto = [ProgrammRead.model_validate(row, from_attributes=True) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto

    @staticmethod
    async def add_programm(programm: ProgrammAdd):
        async with async_session_factory() as session:
            programm_to_add = programm.model_dump()
            
            new_programm = Programm(**programm_to_add)
            session.add(new_programm)
            await session.flush()
            await session.commit()
            await session.refresh(new_programm)
            
            return new_programm.id
