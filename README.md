# AniStation-schedule-api
A simple api created in python which scrapes data from livechart.me to get anime airing schedule.
This is a FastApi app deployed on Render.

# BASE URL
https://anistation-schedule-api.onrender.com/

# Routes
/{season}/{category}
Example: /fall-2023/tv

# Fork and deploy your own instance on Render
uvicorn main:app --host 0.0.0.0 --port 10000
