"""Routes for the FastAPI application Frontend"""

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.fe.fe import get_templates


router = APIRouter(prefix="/myapp")


@router.get("/")
async def get_home_page(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    """Get the home page."""
    result = templates.TemplateResponse("home.html", {"request": request})
    return result
