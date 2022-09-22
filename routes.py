""" Scraper API's."""

from typing import Optional
from fastapi import APIRouter, HTTPException
from .config.database import SessionLocal
from .crud import create_scrapper
from .models import Scraper
from .schemas import ScraperBase, ScraperCreateSchema
from .exceptions import ScrapInfoNotFoundException

app = APIRouter()
session = SessionLocal()

# API endpoint to get info of all scraping pages


@app.get("/scrapp/page")
async def get_scrapps(title: Optional[str] = None):
    """ Get scraping data with pagination API."""
    params = locals().copy()
    query = session.query(Scraper)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Scraper, attr).like(params[attr]))
    session.commit()
    return query.all()

# API endpoint to get info of a scraping page


@app.get("/scrap/{scrap_id}")
async def get_scrap(scrap_id: int):
    """ get specific scraping registrement."""
    db_srap = session.query(Scraper).get(scrap_id)
    if db_srap is None:
        raise ScrapInfoNotFoundException
    return db_srap

# API endpoint for scraping a specific url


@app.post('/scrap')
async def create_new_scrap(url: str):
    """ Create new scrap registrement ."""
    scrap = create_scrapper(
        session, "https://www.facebook.com/footballtunisien.tn/")
    if scrap is None:
        raise ScrapInfoNotFoundException
    return scrap

# GET operation at route '/'


@app.get('/')
def root_api():
    return {"message": "Welcome to scraping facebook public pages universe"}
