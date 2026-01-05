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
