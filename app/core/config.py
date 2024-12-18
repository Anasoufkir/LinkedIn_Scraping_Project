from pydantic import BaseSettings

class Settings(BaseSettings):
    # Configuration générale
    APP_NAME: str = "LinkedIn Scraping API"
    ENVIRONMENT: str = "development"  # Options: "development", "production"
    DEBUG: bool = True

    # Base de données
    DATABASE_URL: str

    # Sécurité
    SECRET_KEY: str = "change_this_to_a_secure_key"

    # Scraping
    LINKEDIN_BASE_URL: str = "https://www.linkedin.com"
    RATE_LIMIT: int = 5  # Nombre de requêtes autorisées par minute

    # Configuration des logs
    LOG_LEVEL: str = "INFO"  # Options: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"

    class Config:
        env_file = ".env"  # Charger les variables depuis un fichier .env

# Instance de configuration
settings = Settings()
