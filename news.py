import pyttsx3
import requests
import json


def get_news():
    url = 'https://newsapi.org/v2/top-headlines?country=ru&apiKey=a7fb6c4a1d3644ac872439d67a0bf250'
    news = requests.get(url).text
    news_dict = json.loads(news)
    articles = news_dict['articles']
    try:

        return articles
    except:
        return False


def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=ru&apiKey=a7fb6c4a1d3644ac872439d67a0bf250'
