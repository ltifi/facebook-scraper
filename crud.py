""" Scraper crud file."""

from sqlalchemy.orm import Session
from models import Scraper
from scrap import Scrap


def create_scraper(session: Session, url: str):
    """ Create a new scraper."""
    try:
        cl = Scrap(url)
        (title_page, nb_likes, nb_followers, location,
         website, email, categorie) = cl.scrap_data()
        db_scraper_info = Scraper(
            title=title_page, nb_likes=nb_likes, nb_followers=nb_followers, location=location, website=website, email=email, categorie=categorie)
        session.add(db_scraper_info)
        session.commit()
        session.refresh(db_scraper_info)
        return db_scraper_info  
    except Exception as e:
        print(e)
