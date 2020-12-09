import pytest
from api.app import create_app


@pytest.fixture
def client(loop, aiohttp_client):
    return loop.run_until_complete(aiohttp_client(create_app()))
