
from fastapi import APIRouter

router = APIRouter()

@router.get("/profiles")
def get_profiles():
    return {"message": "List of profiles"}

@router.post("/profiles")
def create_profile(profile: dict):
    return {"message": "Profile created", "profile": profile}
