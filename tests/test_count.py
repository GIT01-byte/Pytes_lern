import pytest
from src.programms.service import ProgrammService
from src.core.schemas import ProgrammAdd

@pytest.fixture
def programms():
    return [
        ProgrammAdd(id=1, title='Git', author='Linus Torvalds', description='...'),
        ProgrammAdd(id=2, title='Windows', author='Bill Gates', description='...'),
    ]

@pytest.fixture
def empty_programms():
    ProgrammService.clear()

def test_zero_count_programms(empty_programms):
    assert ProgrammService.count() == 0

def test_count_programms(programms, empty_programms):
    for programm in programms:
        ProgrammService.create_programm(programm)

    assert ProgrammService.count() == 2

def test_count_before_delete_programm(programms, empty_programms):
    for programm in programms:
        ProgrammService.create_programm(programm)
    ProgrammService.delete_programm(2)
    
    assert ProgrammService.count() == 1
