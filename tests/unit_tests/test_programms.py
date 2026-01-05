import time
import pytest

from src.programms.service import ProgrammService
from src.core.schemas import ProgrammAdd, ProgrammRead


@pytest.mark.usefixtures("empty_programms")
class TestProgramms:
    @pytest.mark.skipif("config.getoption('--run-obvious-tests') == 'false'")
    def test_zero_count_programms(self):
        print("Run obvious test (zero count programms)")
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
    
    def test_get_all_programms(self, add_programms, read_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        
        all_programms_read = ProgrammService.get_all()
        
        assert len(read_programms) == len(all_programms_read)
        assert [p.model_dump() for p in all_programms_read] == [p.model_dump() for p in read_programms]

    def test_get_programm(self, add_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        
        all_programms_read = ProgrammService.get_all()
        
        assert add_programms[0].title == all_programms_read[0].title\
            and add_programms[0].id == all_programms_read[0].id
        assert add_programms[1].title == all_programms_read[1].title\
            and add_programms[1].id == all_programms_read[1].id

    def test_get_before_delete_programms(self, add_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        
        ProgrammService.clear()
        all_programms = ProgrammService.get_all()
        
        assert len(all_programms) == 0
        assert ProgrammService.count() == 0

    def test_get_undefinded_program(self, add_programms):
        for programm in add_programms:
            ProgrammService.create_programm(programm)
        
        ProgrammService.clear()

        with pytest.raises(NameError, match='No programm found with ID: 9999'):
            ProgrammService.get(9999)

class TestOther:
    @pytest.mark.skipif("config.getoption('--run-slow') == 'false'")
    def test_slow(self):
        time.sleep(3)

    def test_browser(self, browser):
        print(f"\nВыбранный браузер: {browser}")
