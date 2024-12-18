
from pydantic import BaseModel

class ProfileSchema(BaseModel):
    name: str
    title: str
