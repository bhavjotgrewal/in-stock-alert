from typing import List, Union
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def load_data(file: str) -> List[str]:
    """Generates a list of links from a .txt file."""
    with open(file) as f:
        content = [line.rstrip() for line in f]
    return content


def in_stock_checker(link: str) -> List[Union[str, bool]]:
    """A general function that takes a link and determines whether a product is in stock at Newegg.

    Returns the product name on the website, and if it is in stock."""

    try:

        r = requests.get(link)

        soup = BeautifulSoup(r.content, 'lxml')

        name = soup.find('title').text[:-12]

        in_stock = not 'OUT OF STOCK ' == soup.find('div', {'class': 'flags-body has-icon-left '
                                                                     'fa-exclamation-triangle'}). \
            find('span').text

        return [name, in_stock]

    except:
        pass


def in_stock_list(links: list) -> List[List[Union[str, bool]]]:
    """Returns whether products are in stock from a list of links of products."""
    output = []
    for link in links:
        output.append(in_stock_checker(link))
    return output
