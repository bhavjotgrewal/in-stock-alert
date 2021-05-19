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


def in_stock_ps5_disc_updated() -> bool:
    try:
        return not in_stock_ps5_disc() == 'Coming soon'
    except:
        pass
