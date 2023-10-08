from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

@app.get("/{season}/{category}")
async def read_item(season, category):
    return scraper.scrapeScheduleData(season, category)