from fastapi import APIRouter, HTTPException
from app.schemas.profile_schema import ProfileCreate, ProfileResponse
from app.scraper.linkedin_scraper import scrape_profiles

router = APIRouter()

# Route pour récupérer tous les profils
@router.get("/", response_model=list[ProfileResponse])
def get_profiles():
    # Exemple : Récupérer les profils depuis la base de données
    return [{"id": 1, "name": "John Doe", "current_position": "Software Engineer"}]

# Route pour ajouter un nouveau profil
@router.post("/", response_model=ProfileResponse)
def create_profile(profile: ProfileCreate):
    # Exemple : Sauvegarder le profil dans la base de données
    return {"id": 2, "name": profile.name, "current_position": profile.current_position}

# Route pour scraper des profils LinkedIn
@router.get("/scrape", response_model=list[ProfileResponse])
def scrape_profiles_endpoint():
    profiles = scrape_profiles()
    if not profiles:
        raise HTTPException(status_code=404, detail="No profiles found")
    return profiles
