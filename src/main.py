import asyncio
import tracemalloc

from core.schemas import ProgrammAdd
from programms.service import ProgrammService
from programms.repository import ProgrammsRepo

# Включаем отслеживание памяти, для дебага ошибок с ассинхронными функциями
tracemalloc.start()


def main():
    ProgrammsRepo.create_tables()
    
    print(ProgrammService.create_programm(ProgrammAdd(
        id=1, 
        title='Git',
        author='Linus Torvalds', 
        description='Git is a distributed version control software system\
that iscapable of managing versions of source code or data.\
It is often used to control source code by programmers who are developing software collaboratively.'
        ))
    )
    print(ProgrammService.create_programm(ProgrammAdd(
        id=2, 
        title='Git1',
        author='Linus Torvalds Second',
        ))
    )
    print(ProgrammService.get_all())
    print(ProgrammService.count())


if __name__ == "__main__":
    main()
