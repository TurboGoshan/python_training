import requests
from bs4 import BeautifulSoup

def weather1():

    url = 'https://www.meteoprog.lv/ru/weather/Riga/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)

    search = soup.find('div', {'class': 'main-weather__item-temperature'})

    x = search.text

    print('Температура в Риге сейчас: ' + x)
