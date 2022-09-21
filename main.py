# main.py
# Import FastAPI
from fastapi import FastAPI
# from fastapi import APIRouter
import scraper_route as scraperApi

# router = APIRouter()

# router.include_router(scrapperApi.app)


# Initialize the app
app = FastAPI()

app.include_router(scraperApi.app)

