import requests
from bs4 import BeautifulSoup


class BaseConfig:
    HOST = 'https://terrapro.uz'
    HEADERS = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36'

    def base_connect(self):
        request = requests.get(url=self.HOST, headers={'User-Agent': self.HEADERS})
        html = BeautifulSoup(request.text, 'html.parser')
        return html

    def get_status(self):
        request = requests.get(url=self.HOST, headers={'User-Agent': self.HEADERS})
        return request.status_code

    def custom_connect(self, path):
        request = requests.get(url=path, headers={'User-Agent': self.HEADERS})
        html = BeautifulSoup(request.text, 'html.parser')
        return html


base_config = BaseConfig()

