from datetime import date
import os
import requests

MEDIASTACK_KEY = os.environ.get('MEDIASTACK_KEY')
MEDIASTACK_BASE_URL = f'http://api.mediastack.com/v1/news?access_key={MEDIASTACK_KEY}'

def get_news(language, keyword):
    '''
    Returns 100 most popular news stories from today, given the language and keyword.
    '''
    today = date.today().strftime('%Y-%m-%d')
    url = MEDIASTACK_BASE_URL + f'&keywords={keyword}&languages={language}&date={today}&sort=popularity&limit=100'
    
    response = requests.get(url)

    if not response.ok:
        return

    return response.json()['data']

news = get_news('de', 'ukraine')
