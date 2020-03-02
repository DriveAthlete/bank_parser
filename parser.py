import json
import requests


class Parser:
    key = 'df090133a402954859459ca780bb316c'
    base_url = 'https://currate.ru/api/'
    patterns = ('USDEUR', 'USDGBP', 'USDRUB', 'USDBTC')

    def make_str(self):
        STR = '?get=rates&pairs='
        for p in self.patterns:
            STR += (p + ',')

        return STR

    def parse(self):
        responce = requests.get(
            self.base_url + self.make_str() + '&key=' + self.key
        )
        json_array = json.loads(responce.text)
        print(json_array['data'])
        return json_array['data']
