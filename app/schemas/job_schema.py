
from pydantic import BaseModel

class JobSchema(BaseModel):
    title: str
    description: str
