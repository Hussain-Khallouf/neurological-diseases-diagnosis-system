from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.domain.schema.symptom import SymptomIn
from app.domain.usecase.symptom_uc import SymptomUC
from ..dependencies import get_symptom_repo
from app.domain.interface.symptom_repo import SymptomRepository
from app.config.settings import settings

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/start", response_class=HTMLResponse)
def start(
    request: Request, symptom_repo: SymptomRepository = Depends(get_symptom_repo)
):
    sympotm_uc = SymptomUC(symptom_repo)
    symptom = sympotm_uc.get_next_symptom()
    return templates.TemplateResponse(
        "symptom.html", {"request": request, "base_url": settings.BASE_URL, "name": symptom.name}
    )

@router.post("/diagnosis", response_class=HTMLResponse)
def diagno(
    request: Request,
    symptom_repo: SymptomRepository = Depends(get_symptom_repo),
    name: str = Form(...),
    answer: str = Form(...),
):
    symptom_us = SymptomUC(symptom_repo)
    symptom_in = SymptomIn(name=name, answer=answer)
    result, next_symptom = symptom_us.add_symptom(symptom_in)
    if result is not None:
        return templates.TemplateResponse(
            "result.html", {"request": request, "result": result.disease}
        )
    return templates.TemplateResponse(
        "symptom.html", {"request": request, "base_url": settings.BASE_URL, "name": next_symptom.name}
    )
