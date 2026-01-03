import asyncio
import tracemalloc

from programms.service import ProgrammService
from programms.repository import ProgrammsRepo

# Включаем отслеживание памяти, для дебага ошибок с ассинхронными функциями
tracemalloc.start()


async def main():
    await ProgrammsRepo.create_tables()
    
    await ProgrammService.create_programm(
        id=2, 
        title='Git',
        author='Linus Torvalds', 
        description='Git is a distributed version control software system\
that iscapable of managing versions of source code or data.\
It is often used to control source code by programmers who are developing software collaboratively.'
    )
    await ProgrammService.get_all()


if __name__ == "__main__":
    asyncio.run(main()) 
