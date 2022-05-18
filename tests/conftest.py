import pytest
from Steam2 import app as _app


@pytest.fixture
def app():
    """Create and configure new app instances for each test."""
    return _app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
