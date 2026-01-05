import pytest
from src.programms.service import ProgrammService
from src.core.schemas import ProgrammAdd, ProgrammRead


@pytest.fixture(scope="function")
def empty_programms():
    ProgrammService.clear()

@pytest.fixture
def add_programms():
    return [
        ProgrammAdd(id=1, title='Git', author='Linus Torvalds', description='...', license_key='11-12-12-1'),
        ProgrammAdd(id=2, title='Windows', author='Bill Gates', license_key='11-12-12-2'),
    ]

@pytest.fixture
def read_programms():
    return [
        ProgrammRead(id=1, title='Git', author='Linus Torvalds', description='...'),
        ProgrammRead(id=2, title='Windows', author='Bill Gates', description='N/A'),
    ]
