import time
import pytest

from src.core.db import sync_engine
from src.core.models import Base

from src.core.config import settings


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    print(f"{settings.DB_NAME=}")
    assert settings.MODE == 'TEST'
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def pytest_addoption(parser):
    # Регистрируем браузер
    parser.addoption(
        "--browser",
        default='chrome',
        choices=("chrome", "mozilla"),
        help="Выбор браузера: chrome или mozilla"
    )
    # Регистрируем медленные тесты
    parser.addoption(
        "--run-slow",
        default='true',
        choices=("true", "false"),
        help="Запускать ли медленные тесты: true или false"
    )
    # Регистрируем очевидные тесты
    parser.addoption(
        "--run-obvious-tests",
        default='true',
        choices=("true", "false"),
        help="Запускать ли очевидные=ные тесты: true или false"
    )

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
