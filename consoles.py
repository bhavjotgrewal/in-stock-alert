from bs4 import BeautifulSoup
import requests
from datetime import datetime


def in_stock_ps5_disc() -> str:
    """Returns whether the PS5 (disc) is in stock at the following retailers:
    - Bestbuy

    More retailers coming soon!
    """

    url = 'https://www.bestbuy.ca/en-ca/product/playstation-5-console-online-only/14962185'

    # add header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    result = soup.find('div', {'class': 'availabilityMessageProduct_ZCIQp'}).text

    return result


def in_stock_ps5_digital() -> str:
    """Returns whether the PS5 (disc) is in stock at the following retailers:
    - Bestbuy

    More retailers coming soon!
    """

    url = 'https://www.bestbuy.ca/en-ca/product/playstation-5-digital-edition-console-online-only' \
          '/14962184 '

    # add header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    result = soup.find('div', {'class': 'availabilityMessageProduct_ZCIQp'}).text

    return result


def notifier():
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if in_stock_ps5_digital() == 'Coming soon':
            print('\x1b[0;30;44m' + 'Bestbuy' + '\x1b[0m' + ' PS5 Disc ' + '\x1b[0;30;41m' +
                  'out of stock' + '\x1b[0m' + ' ' + dt_string)
        else:
            print('\x1b[0;30;44m' + 'Bestbuy' + '\x1b[0m' + ' PS5 Disc ' + '\x1b[0;30;42m' +
                  'in stock' + '\x1b[0m' + ' ' + dt_string)
        if in_stock_ps5_disc() == 'Coming soon':
            print('\x1b[0;30;44m' + 'Bestbuy' + '\x1b[0m' + ' PS5 Digital ' + '\x1b[0;30;41m' +
                  'out of stock' + '\x1b[0m' + ' ' + dt_string)
        else:
            print('\x1b[0;30;44m' + 'Bestbuy' + '\x1b[0m' + ' PS5 Digital ' + '\x1b[0;30;42m' +
                  'in stock' + '\x1b[0m' + ' ' + dt_string)
