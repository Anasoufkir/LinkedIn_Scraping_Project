from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    company_id: Optional[int] = None  # Référence à une entreprise

    class Config:
        schema_extra = {
            "example": {
                "title": "Backend Developer",
                "description": "Develop and maintain backend services",
                "location": "Remote",
                "company_id": 1
            }
        }

class JobResponse(JobCreate):
    id: int  # Identifiant de l'offre d'emploi

    class Config:
        orm_mode = True
