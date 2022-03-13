from ast import keyword
from re import L
from helpers.textblob_helper import translate, LANGUAGES
from helpers.news_helper import get_news

news_by_country = {}
for lang in LANGUAGES.items():
    keyword = 'russia' if lang[0] == 'en' else translate('russia', lang[1], 'en')

    raw_news = get_news(lang[0], keyword)
    if raw_news is None:
        continue

    for news in raw_news:
        if news_by_country.get(news['country']) is None:
            news_by_country[news['country']] = ''

        news_by_country[news['country']] += f'{news["title"]} {news["description"]}'

print(news_by_country)
