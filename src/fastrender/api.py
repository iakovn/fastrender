from fastapi import FastAPI

from . import __version__
from .schemas import VersionResponse

app = FastAPI(title="fastrender")


@app.get("/version", response_model=VersionResponse)
def get_version():
    """Return the package version."""
    return VersionResponse(version=__version__)
