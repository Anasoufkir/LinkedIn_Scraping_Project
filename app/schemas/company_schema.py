from pydantic import BaseModel
from typing import Optional

class CompanyCreate(BaseModel):
    name: str
    sector: str
    location: Optional[str] = None
    employees_count: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "TechCorp",
                "sector": "Information Technology",
                "location": "New York",
                "employees_count": 250
            }
        }

class CompanyResponse(CompanyCreate):
    id: int  # Identifiant de l'entreprise

    class Config:
        orm_mode = True
