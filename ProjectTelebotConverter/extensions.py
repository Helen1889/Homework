import requests
import json
from configs import keys

class ConvertionException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f"Введена одна и та же валюта: {base}")

        try:
            quo_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Валюта {quote} недоступна для конвертации")
        try:
            ba_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Валюта {base} недоступна для конвертации")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")
        r = requests.get(f"https://api.currencyapi.com/v3/latest?apikey=cur_live_TRRn8oCA6R0oeHMoqFlLQ4tDn6mfmKbWdpx5lzjN")
        text1 = json.loads(r.content)["data"][f'{quo_ticker}']['value']
        text2 = json.loads(r.content)["data"][f'{ba_ticker}']['value']
        text_total = (float(amount) * text2) / text1
        return text_total