from typing import List, Union
import requests
from bs4 import BeautifulSoup


def in_stock_checker(link: str) -> List[Union[str, bool, int]]:
    """A general function that takes a link and determines whether a product is in stock at
    Memory Express.

    Returns the product name on the website, and if it is in stock."""

    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        r = requests.get(link, headers=headers)

        soup = BeautifulSoup(r.content, 'lxml')

        name = soup.find('title').text[:-43]

        if soup.find('div',
                     {'class': 'c-capr-inventory-store'}).find(
            'span',
            {'class': 'c-capr-inventory-store__availability InventoryState_OutOfStock'}) is \
                None:
            in_stock = True
            quantity = soup.find('div',
                                 {'class': 'c-capr-inventory-selector__details-online'}).find('div',
                                                                                              {
                                                                                                  'class': 'c-capr-inventory-store'}).find(
                'span',
                {'class': 'c-capr-inventory-store__availability InventoryState_InStock'}).text[
                       14:15]
        else:
            in_stock = False
            quantity = 0

        return [name, in_stock, quantity]

    except:
        print('connection blocked')
        pass
