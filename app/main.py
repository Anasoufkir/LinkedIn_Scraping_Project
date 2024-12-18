
from fastapi import FastAPI
from app.api import profiles, companies, jobs

app = FastAPI()

app.include_router(profiles.router, prefix="/api/v1")
app.include_router(companies.router, prefix="/api/v1")
app.include_router(jobs.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the LinkedIn Scraping API"}
