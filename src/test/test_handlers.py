import pytest

from fastapi.testclient import TestClient
import pytest_asyncio

from myapi.app import app, settings


@pytest.fixture
def client():
    # Use the client within a context manager
    # so that FastAPI will process events
    with TestClient(app) as client:
        yield client


def test_hello_world_debug_off(client):
    res = client.get("/")
    assert res.text == '"Ok."'


def test_hello_world_debug_on(client):
    settings.debug = True
    res = client.get("/")
    assert "uptime" in res.json()
