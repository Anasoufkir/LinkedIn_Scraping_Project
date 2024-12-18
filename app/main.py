from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import profiles, companies, jobs
from app.core.database import Base, engine
from app.core.config import settings
# Créer l'application FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description="API for LinkedIn scraping and data management",
    version="1.0.0",
    debug=settings.DEBUG
)

# Configurer CORS (Cross-Origin Resource Sharing)
origins = ["*"]  # À limiter aux domaines spécifiques en production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
app.include_router(companies.router, prefix="/companies", tags=["Companies"])
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])

# Initialiser la base de données
@app.on_event("startup")
def startup_event():
    """Créer les tables de la base de données au démarrage."""
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown_event():
    """Nettoyer les ressources si nécessaire lors de l'arrêt."""
    pass

# Endpoint de santé
@app.get("/")
def root():
    """Endpoint pour vérifier que l'API fonctionne."""
    return {"message": f"Welcome to {settings.APP_NAME}!"}
