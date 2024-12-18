from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    current_position = Column(String, nullable=False)
    skills = Column(String, nullable=True)  # Stocke les compétences sous forme de texte séparé par des virgules
    experience = Column(String, nullable=True)  # Expériences passées

    # Relation avec les entreprises si nécessaire
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="employees")
