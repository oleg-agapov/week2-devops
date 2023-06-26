import pytest
from quote_gen.app import app


@pytest.fixture
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


def test_home_page(test_client):
    res = test_client.get("/")
    assert res.status_code == 200

def test_health_page(test_client):
    res = test_client.get("/health")
    assert res.status_code == 200
    assert "healthy" in str(res.data)

def test_quote_page(test_client):
    res = test_client.get("/quote")
    assert res.status_code == 200
