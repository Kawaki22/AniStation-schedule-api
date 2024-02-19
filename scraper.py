from fastapi import FastAPI
from requests_html import HTMLSession

class Scraper():
    def scrapeScheduleData(self, season, category):
        url = f'https://www.livechart.me/{season}/{category}'
        response = HTMLSession().get(url)
        
        card = response.html.find('div.anime-card')
        schedule_list = []
        
        for c in card:
            episode_countdown = c.find('time.text-bold', first = True)
        
            if episode_countdown is not None:
                
                image = c.find('img', first = True).attrs.get('srcset').split("1x, ")
                episode_split = c.find('div.release-schedule-info', first = True).text.strip()
                index = episode_split.find(' · ')
                episode = episode_split[:index]
                # match = re.match(r'EP(\d+): (.+)', countdown_text.text)

                items = {
                    'episodeAndTimestamp' : 'N/A',
                    'episode' : episode,
                    'timeStamp' : episode_countdown.attrs.get('data-timestamp'),
                    'title' : c.find('h3.main-title', first = True).text.strip(),
                    'imageUrl' : image[1],
                    'rating' : c.find('div.anime-extras', first = True).text.strip(),
                    'animeStudio' : c.find('ul.anime-studios', first = True).text.strip()
                }
                schedule_list.append(items)
        return schedule_list
            

# schedule = Scraper()
# schedule.scrapeScheduleData('winter-2024', 'tv')