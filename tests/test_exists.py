from Steam2 import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_app_exists(app):
    assert app is not None


def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert "<title>QR</title>".encode() in rv.data
