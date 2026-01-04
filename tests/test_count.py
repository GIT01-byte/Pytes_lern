import pytest

from src.programms.service import ProgrammService
from src.programms.repository import ProgrammsRepo


@pytest.mark.asyncio
async def test_count_programms():
    await ProgrammService.clear()
    await ProgrammService.create_programm(
        id=1, 
        title='Git',
        author='Linus Torvalds', 
        description='Git is a distributed version control software system\
that iscapable of managing versions of source code or data.\
It is often used to control source code by programmers who are developing software collaboratively.'
    )
    await ProgrammService.create_programm(
        id=2, 
        title='Git1',
        author='Linus Torvalds 1', 
        description='Git is a distributed version control software system\
that iscapable of managing versions of source code or data.\
It is often used to control source code by programmers who are developing software collaboratively..'
    )
    assert await ProgrammService.count() == 2