from fastapi import APIRouter, HTTPException
from app.schemas.job_schema import JobCreate, JobResponse
from app.scraper.linkedin_scraper import scrape_jobs

router = APIRouter()

# Route pour récupérer toutes les offres d'emploi
@router.get("/", response_model=list[JobResponse])
def get_jobs():
    # Exemple : Récupérer les offres d'emploi depuis la base de données
    return [{"id": 1, "title": "Backend Developer", "company": "TechCorp", "location": "Remote"}]

# Route pour ajouter une nouvelle offre d'emploi
@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate):
    # Exemple : Sauvegarder l'offre d'emploi dans la base de données
    return {"id": 2, "title": job.title, "company": job.company, "location": job.location}

# Route pour scraper des offres d'emploi LinkedIn
@router.get("/scrape", response_model=list[JobResponse])
def scrape_jobs_endpoint():
    jobs = scrape_jobs()
    if not jobs:
        raise HTTPException(status_code=404, detail="No jobs found")
    return jobs
