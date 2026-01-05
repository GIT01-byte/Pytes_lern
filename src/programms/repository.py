from sqlalchemy import and_, func, select, delete

from core.db import Base, sync_engine, session_factory

from core.models import Programm
from core.schemas import ProgrammRead, ProgrammAdd


class ProgrammsRepo:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def get_all_programms():
        with session_factory() as session:
            query = select(Programm)
            res = session.execute(query)
            result_orm = res.scalars().all()
            print(f"{result_orm=}")

            result_dto = [ProgrammRead.model_validate(row, from_attributes=True) for row in result_orm]
            print(f"{result_dto=}")
            return result_dto

    @staticmethod
    def add_programm(programm: ProgrammAdd):
        with session_factory() as session:
            programm_to_add = programm.model_dump()
            
            new_programm = Programm(**programm_to_add)
            session.add(new_programm)
            session.flush()
            session.commit()
            session.refresh(new_programm)
            
            print(f'Add programm: {new_programm.title}, ID: {new_programm.id}')
            return new_programm.id

    @staticmethod
    def delete_programm(programm_id: int):
        with session_factory() as session:
            # Выполнить запрос для выбора программы по id
            query = select(Programm).where(Programm.id == programm_id)
            result = session.execute(query)
            programm = result.scalar_one_or_none()
            
            if programm:
                # Удалить найденную программу
                session.delete(programm)
                session.commit()  # Или flush(), если хотите отложить commit
                print(f'Deleted programm with ID: {programm_id}')
            else:
                print(f'No programm found with ID: {programm_id}')

    @staticmethod
    def delete_all():
        with session_factory() as session:
            query = select(Programm)
            res = session.execute(query)
            items_to_delete = res.scalars().all()
            
            delete_count = 0
            for item in items_to_delete:
                session.delete(item)
                delete_count += 1
            
            print(f'Delete all programm rows, count deleted rows: {delete_count}')
            session.commit()

    @staticmethod
    def count_of_programms():
        with session_factory() as session:
            query = select(func.count()).select_from(Programm)
            res = session.execute(query)
            count = res.scalar()
            print(f'Count of all programms: {count}')
            return count
