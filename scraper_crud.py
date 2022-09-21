""" Episode crud file."""

from sqlalchemy.orm import Session
from scraper_schema import ScraperCreateSchema
from scraper_model import Scraper


def create_scrapper(session: Session, scrapper_data: ScraperCreateSchema):
    """ Create a new scrapper."""
    db_scrapper_info = Scraper(title=scrapper_data.title)
    session.add(db_scrapper_info)
    session.commit()
    session.refresh(db_scrapper_info)
    return db_scrapper_info
