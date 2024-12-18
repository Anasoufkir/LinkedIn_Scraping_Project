
from fastapi import APIRouter

router = APIRouter()

@router.get("/companies")
def get_companies():
    return {"message": "List of companies"}

@router.post("/companies")
def create_company(company: dict):
    return {"message": "Company created", "company": company}
