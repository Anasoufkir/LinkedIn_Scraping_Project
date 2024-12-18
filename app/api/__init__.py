from fastapi import APIRouter
from app.api import profiles, companies, jobs

router = APIRouter()

# Enregistrement des routes pour chaque entité
router.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
router.include_router(companies.router, prefix="/companies", tags=["Companies"])
router.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
