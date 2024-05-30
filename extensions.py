import configparser

import lxml.html
import requests

config = configparser.ConfigParser()


def get_text(_key: str, _item: str) -> str:
    config.read('text.ini', encoding="utf8")
    return config[_key][_item]


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


class Values:
    def __init__(self) -> None:
        self._values = {
            "руб": "RUB",
            "дол": "USD",
            "евр": "EUR",
            "фун": "GBP",
            "фра": "CHF",
            "юан": "CNY",
        }

    def check_str(self, _str: str) -> bool:
        _str = _str.lower()[:3]
        return _str in self._values

    def get_price(self, _base: str, _quote: str, _amount: float) -> str:
        _base = self._values[_base.lower()[:3]]
        _quote = self._values[_quote.lower()[:3]]
        html = requests.get(f'https://www.x-rates.com/calculator/?from={_base}&to={_quote}&amount={_amount}').content
        tree = lxml.html.document_fromstring(html)
        ms_left = tree.xpath('//*[@id="content"]/div[1]/div/div[1]/div/div/span[1]/text()')[0]
        ms_right = tree.xpath('//*[@id="content"]/div[1]/div/div[1]/div/div/span[2]/text()')[0]
        return f"{ms_left} {ms_right} {_quote} "

    def __str__(self) -> str:
        ms = [get_text("values", item) for item in self._values.values()]
        return f" \n".join(ms)

