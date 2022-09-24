""" Scraper API's."""

from typing import Optional
from fastapi import APIRouter
from config.database import SessionLocal
from crud import create_scraper
from models import Scraper
from exceptions import ScrapInfoNotFoundException
from starlette import status

app = APIRouter()
session = SessionLocal()

# API endpoint to get info of all scraping pages


@app.get("/scrap/page", status_code=status.HTTP_201_CREATED)
async def get_scraps(title: Optional[str] = None):
    """ Get scraping data with pagination API."""
    params = locals().copy()
    query = session.query(Scraper)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Scraper, attr).like(params[attr]))
    session.commit()
    return query.all()

# API endpoint to get info of a scraping page


@app.get("/scrap/{scrap_id}", status_code=status.HTTP_200_OK)
async def get_scrap(scrap_id: int):
    """ get specific scraping registrement."""
    db_srap = session.query(Scraper).get(scrap_id)
    if db_srap is None:
        raise ScrapInfoNotFoundException
    return db_srap

# API endpoint for scraping a specific url


@app.post('/scrap', status_code=status.HTTP_201_CREATED)
async def create_new_scrap():
    """ Create new scrap registrement ."""
    scrap = create_scraper(
        session, "https://www.facebook.com/footballtunisien.tn/")
    if scrap is None:
        raise ScrapInfoNotFoundException
    return scrap

# GET operation at route '/'


@app.get('/')
def root_api():
    return {"message": "Welcome to scraping facebook public pages universe"}
