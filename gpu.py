from bs4 import BeautifulSoup
import requests
from datetime import datetime


def in_stock_tuf_3080() -> str:
    """Returns whether the RTX 3080 TUF OC is in stock at Newegg"""

    r = requests.get('https://www.newegg.ca/asus-geforce-rtx-3080-tuf-rtx3080-o10g-gaming/p'
                     '/N82E16814126452?Description=rtx%203080%20tuf%20oc&cm_re=rtx_3080%20tuf'
                     '%20oc-_-14-126-452-_-Product')

    soup = BeautifulSoup(r.text, 'html.parser')

    result = soup.find('div', {'class': 'flags-body has-icon-left fa-exclamation-triangle'}).find(
        'span').text

    return result

def notifier():
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            if in_stock_tuf_3080() == 'OUT OF STOCK ':
                print(
                    '\x1b[0;30;43m' + 'Newegg' + '\x1b[0m' + ' RTX 3080 TUF OC ' + '\x1b[0;30;41m' +
                    'out of stock' + '\x1b[0m' + ' ' + dt_string)
            else:
                print(
                    '\x1b[0;30;43m' + 'Newegg' + '\x1b[0m' + ' RTX 3080 TUF OC ' + '\x1b[0;30;42m' +
                    'in stock' + '\x1b[0m' + ' ' + dt_string)
        except:
            continue