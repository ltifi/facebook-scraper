""" Scrapper Schema ."""

from pydantic import BaseModel

class ScraperBase(BaseModel):
    """ Scrapper Base Schema ."""
    title: str

class ScraperCreateSchema(BaseModel):
    """ Scraper Create Schema ."""
    url:str