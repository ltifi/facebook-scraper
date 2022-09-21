""" Episodes API's."""

from typing import Optional
from fastapi import APIRouter
from config.database import SessionLocal
from scraper_crud import create_scrapper
from scraper_model import Scraper
from scraper_schema import ScraperBase, ScraperCreateSchema

app = APIRouter()
session = SessionLocal()


@app.get("/scrapp/page")
async def get_scrapps(title: Optional[str] = None):
    """ Get episodes with pagination API."""
    params = locals().copy()
    query = session.query(Scraper)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Scraper, attr).like(params[attr]))
    session.commit()
    return query.all()


@app.get("/scrap", response_model=ScraperBase)
async def get_scrap(scrap_id: int):
    """ get specific scraping registrement."""
    db_srap = session.query(Scraper).get(scrap_id)
    return db_srap


@app.post('/create_new_scrap')
def create_character_scrap(scrap: ScraperCreateSchema):
    """ Create new scrap registrement ."""
    scrap = create_scrapper(session, scrap)
    return scrap

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Welcome to scraping facebook public pages universe"}