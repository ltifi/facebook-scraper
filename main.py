# main.py

from fastapi import FastAPI
import routes as scraperApi

# Initialize the app
app = FastAPI()

app.include_router(scraperApi.app)