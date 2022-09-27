""" Post API's."""

from typing import Optional
from fastapi import APIRouter
from config.database import SessionLocal
from crud import create_scraper
from models import Posts
from exceptions import ScrapInfoNotFoundException
from starlette import status

app = APIRouter()
session = SessionLocal()

# API endpoint to get info of all scraping pages


@app.get("/scrap/page", status_code=status.HTTP_201_CREATED)
async def get_scraps(title: Optional[str] = None):
    """ Get scraping data with pagination API."""
    params = locals().copy()
    query = session.query(Posts)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Posts, attr).like(params[attr]))
    session.commit()
    return query.all()

# API endpoint to get info of a scraping page


@app.get("/scrap/{scrap_id}", status_code=status.HTTP_200_OK)
async def get_scrap(scrap_id: int):
    """ get specific scraping registrement."""
    db_srap = session.query(Posts).get(scrap_id)
    if db_srap is None:
        raise ScrapInfoNotFoundException
    return db_srap

# API endpoint for scraping a specific facebook page


@app.post('/scrap/{page_name}', status_code=status.HTTP_201_CREATED)
async def create_new_scrap(page_name: str):
    """ Create new scrap registrement ."""
    try:
        return create_scraper(session, "https://m.facebook.com/"+page_name)
    except Exception as e:
        print(e)

# GET operation at route '/'


@app.get('/')
def root_api():
    return {"message": "Welcome to scraping facebook public pages universe"}
