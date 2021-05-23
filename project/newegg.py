from typing import List, Union
import requests
from bs4 import BeautifulSoup


def in_stock_checker(link: str) -> List[Union[str, bool]]:
    """A general function that takes a link and determines whether a product is in stock at Newegg.

    Returns the product name on the website, and if it is in stock."""

    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                          'like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        r = requests.get(link, headers=headers)

        soup = BeautifulSoup(r.text, 'lxml')

        name = soup.find('title').text[:-12]

        in_stock = not 'OUT OF STOCK ' == soup.find('div', {'class': 'flags-body has-icon-left '
                                                                     'fa-exclamation-triangle'}). \
            find('span').text

        return [name, in_stock]

    except:
        print('connection blocked')
        pass
