"""Frontend configuration."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



def configure_frontend(app: FastAPI):
    """Setup static files for the app."""
    app.mount("/static", StaticFiles(directory="src/fe/static"), name="static")


def get_templates() -> Jinja2Templates:
    """Get the Jinja2Templates object."""
    return Jinja2Templates(directory="src/fe/templates")