from fastapi import APIRouter, HTTPException
from app.schemas.company_schema import CompanyCreate, CompanyResponse
from app.scraper.linkedin_scraper import scrape_companies

router = APIRouter()

# Route pour récupérer toutes les entreprises
@router.get("/", response_model=list[CompanyResponse])
def get_companies():
    # Exemple : Récupérer les entreprises depuis la base de données
    return [{"id": 1, "name": "TechCorp", "sector": "IT", "location": "New York"}]

# Route pour ajouter une nouvelle entreprise
@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate):
    # Exemple : Sauvegarder l'entreprise dans la base de données
    return {"id": 2, "name": company.name, "sector": company.sector, "location": company.location}

# Route pour scraper des entreprises LinkedIn
@router.get("/scrape", response_model=list[CompanyResponse])
def scrape_companies_endpoint():
    companies = scrape_companies()
    if not companies:
        raise HTTPException(status_code=404, detail="No companies found")
    return companies
