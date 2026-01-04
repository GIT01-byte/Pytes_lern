import pytest
from src.programms.service import ProgrammService
from src.core.schemas import ProgrammAdd

@pytest.fixture(scope="session") # Можно сделать session, раз данные общие
def programms():
    return [
        ProgrammAdd(id=1, title='Git', author='Linus Torvalds', description='...'),
        ProgrammAdd(id=2, title='Windows', author='Bill Gates', description='...'),
    ]

@pytest.mark.asyncio
async def test_zero_count_programms():
    await ProgrammService.clear()
    assert await ProgrammService.count() == 0

@pytest.mark.asyncio
async def test_count_programms(programms):
    await ProgrammService.clear()
    for programm in programms:
        await ProgrammService.create_programm(programm)

    assert await ProgrammService.count() == 2

@pytest.mark.asyncio
async def test_count_before_delete_programm(programms):
    await ProgrammService.clear()
    for programm in programms:
        await ProgrammService.create_programm(programm)
    await ProgrammService.delete_programm(2)
    
    assert await ProgrammService.count() == 1
