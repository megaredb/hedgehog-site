from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from utils import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/{tome_id}", response_class=HTMLResponse)
async def tome_page(tome_id: int, request: Request):
    return templates.TemplateResponse(
        "tome.html", {"request": request, "tome": {"id": tome_id, "name": "Том 1"}}
    )
