import pytest
from src.programms.service import ProgrammService
from src.core.schemas import ProgrammAdd, ProgrammRead

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

@pytest.fixture
def empty_programms():
    ProgrammService.clear()

@pytest.mark.usefixtures("empty_programms")
class TestProgramms:
    def test_zero_count_programms(self):
        assert ProgrammService.count() == 0
    
    def test_count_programms(self, add_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)

        assert ProgrammService.count() == 2

    def test_count_before_delete_programm(self, add_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        ProgrammService.delete_programm(2)
        
        assert ProgrammService.count() == 1
    
    def test_get_programms(self, add_programms, read_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        
        all_programms_read = ProgrammService.get_all()
        
        assert len(read_programms) == len(all_programms_read)
        assert [p.model_dump() for p in all_programms_read] == [p.model_dump() for p in read_programms]

