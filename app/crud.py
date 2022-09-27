""" Scraper crud file."""

from sqlalchemy.orm import Session
from models import Posts
from scrap import Scrap


def create_scraper(session: Session, url: str):
    """ Create a new scraper."""
    try:
        cl = Scrap(url)
        (post_links, texts, likes, comments, dates, times) = cl.scrap_data()
        for c in range(len(post_links)):
            db_scraper_info = Posts(
                link=post_links[c], text=texts[c], nb_likes=likes[c], nb_comments=comments[c], date=dates[c], time=times[c])
            session.add(db_scraper_info)
            session.commit()
            session.refresh(db_scraper_info)
    except Exception as e:
        print(e)
