from pydantic import BaseModel
from typing import List, Optional

class ProfileCreate(BaseModel):
    name: str
    current_position: str
    skills: Optional[List[str]] = None  # Liste des compétences
    experience: Optional[List[str]] = None  # Liste des expériences passées

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "current_position": "Software Engineer",
                "skills": ["Python", "FastAPI", "SQL"],
                "experience": ["Company A", "Company B"]
            }
        }

class ProfileResponse(ProfileCreate):
    id: int  # Identifiant du profil

    class Config:
        orm_mode = True
