# AniStation-schedule-api
A simple api created in python which scrapes data from livechart.me to get anime airing schedule.
This is a FastApi app deployed on Render.

<p align="center">
    <a href="https://github.com/Kawaki22/AniStation-schedule-api/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/consumet/api" alt="GitHub">
  </a>
</p>

# BASE URL
https://anistation-schedule-api.onrender.com/

# Routes
/{season}/{category}
Example: /fall-2023/tv

# Deploy your own instance on Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FKawaki22%2FAniStation-schedule-api)

# Deploy your own instance on Render

Start Command:
```sh
uvicorn main:app --host 0.0.0.0 --port 10000
```

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Kawaki22/AniStation-schedule-api)
