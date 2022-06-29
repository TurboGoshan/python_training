import requests
from bs4 import BeautifulSoup


def course1():
    url = 'https://finance.rambler.ru/currencies/EUR/'

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text)

    search = soup.find('div', {'class': 'finance-currency-plate'})

    main = search.text

    x = main[115:130]

    print('Курс евро на сегодня = ' + x + ' ' + 'Изменения курса')
