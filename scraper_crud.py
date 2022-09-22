""" Scraper crud file."""

from sqlalchemy.orm import Session
from scraper_schema import ScraperCreateSchema
from scraper_model import Scraper
from scrap import Scrap


def create_scrapper(session: Session, url: str):
    """ Create a new scrapper."""
    cl = Scrap(url)
    (title_page, nb_likes, nb_followers, location,
     website, email, categorie) = cl.get_browser()
    print("title is :", title_page)
    db_scraper_info = Scraper(
        title=title_page, nb_likes=nb_likes, nb_followers=nb_followers, location=location, website=website, email=email, categorie=categorie)
    session.add(db_scraper_info)
    session.commit()
    session.refresh(db_scraper_info)
    return db_scraper_info


# def
# cl = Scraper(url="https://www.facebook.com/footballtunisien.tn/")
# cl.get_browser()
