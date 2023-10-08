from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

@app.get("/")
async def read_item():
    return "Welcome to AniStation Schedule Api 🎉"

@app.get("/{season}/{category}")
async def read_item(season, category):
    return scraper.scrapeScheduleData(season, category)