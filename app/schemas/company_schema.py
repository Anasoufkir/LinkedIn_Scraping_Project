
from pydantic import BaseModel

class CompanySchema(BaseModel):
    name: str
    industry: str
