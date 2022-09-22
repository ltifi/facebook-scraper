""" Scraper API's."""

from typing import Optional
from fastapi import APIRouter, HTTPException
from config.database import SessionLocal
from scraper_crud import create_scrapper
from scraper_model import Scraper
from scraper_schema import ScraperBase, ScraperCreateSchema

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
        raise HTTPException(
            status_code=404, detail="Input not found")
    return db_srap

# API endpoint for scraping a specific url


@app.post('/scrap')
async def create_new_scrap(url: str):
    """ Create new scrap registrement ."""
    scrap = create_scrapper(
        session, "https://www.facebook.com/footballtunisien.tn/")
    if scrap is None:
        raise HTTPException(
            status_code=404, detail="Input scraped not registered")
    return scrap

# GET operation at route '/'


@app.get('/')
def root_api():
    return {"message": "Welcome to scraping facebook public pages universe"}
