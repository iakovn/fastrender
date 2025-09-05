from fastapi.testclient import TestClient

from fastrender import __version__
from fastrender.api import app

client = TestClient(app)


def test_version_endpoint():
    resp = client.get("/version")
    assert resp.status_code == 200
    assert resp.json() == {"version": __version__}
