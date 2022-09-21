""" scrapings model."""

from sqlalchemy import Column, Integer, String
from config.database import engine, Base


class Scraper(Base):
    """ Create scraper model."""
    __tablename__ = "scraper"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=False, index=False, nullable=False)


Base.metadata.create_all(engine)
