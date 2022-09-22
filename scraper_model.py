""" scrapings model."""

from sqlalchemy import Column, Integer, String
from config.database import engine, Base


class Scraper(Base):
    """ Create scraper model."""
    __tablename__ = "scraper"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=False)
    nb_likes = Column(Integer)
    nb_followers = Column(Integer)
    location = Column(String(80))
    website = Column(String(60))
    email = Column(String(50))
    categorie = Column(String(50))



Base.metadata.create_all(engine)
