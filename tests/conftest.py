import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry
from src.fast_zero.app import app
from src.fast_zero.settings import Settings


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db_session():
    engine = create_engine(Settings().URL_DB_TEST)
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)


@pytest.fixture
def user_test():
    user = User(
        username='testusername',
        email='teste@teste.com',
        password='secret',
    )

    return user
