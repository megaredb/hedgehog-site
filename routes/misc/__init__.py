from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from utils import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
