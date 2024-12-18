from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    sector = Column(String, nullable=False)
    location = Column(String, nullable=True)
    employees_count = Column(Integer, nullable=True)

    # Relation avec les employés (profils)
    employees = relationship("Profile", back_populates="company")
