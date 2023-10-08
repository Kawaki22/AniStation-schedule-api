from fastapi import FastAPI
from requests_html import HTMLSession
import re

class Scraper():
    def scrapeScheduleData(self, season, category):
        url = f'https://www.livechart.me/{season}/{category}'
        s = HTMLSession().get(url)
        
        card = s.html.find('div.anime-card')
        schedule_list = []
        
        for c in card:
            episode_countdown = c.find('time.episode-countdown', first = True)
        
            if episode_countdown is not None:
                
                # match = re.match(r'EP(\d+): (.+)', countdown_text.text)

                items = {
                    'episodeAndTimestamp' : c.find('time.episode-countdown', first = True).text.strip(),
                    'title' : c.find('h3.main-title', first = True).text.strip(),
                    'imageUrl' : {
                        c.find('img', first = True).attrs.get('srcset')
                    },
                    'rating' : c.find('div.anime-extras', first = True).text.strip(),
                    'animeStudio' : c.find('ul.anime-studios', first = True).text.strip()
                   
                }
                schedule_list.append(items)
        return schedule_list
            

# schedule = Scraper()
# schedule.scrapeScheduleData('fall-2023', 'tv')