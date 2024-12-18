from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location = Column(String, nullable=True)

    # Relation avec l'entreprise
    company_id = Column(Integer, ForeignKey("companies.id"))
    company = relationship("Company", back_populates="jobs")
