from requests import Session
from bs4 import BeautifulSoup
from os import environ


class Account(Session):
    def __init__(self, username, password):
        Session.__init__(self)

        iproyal_username = environ['ip_royal_username']
        iproyal_password = environ['ip_royal_password']

        # self.proxies = {
        #     'http': f'http://{iproyal_username}:{iproyal_password}@geo.iproyal.com:22323',
        #     'https': f'http://{iproyal_username}:{iproyal_password}@geo.iproyal.com:22323'
        # }

        self.username = username
        self.password = password

    def login(self):
        login_page = self.get('https://www.reddit.com/login/')
        soup = BeautifulSoup(login_page.content, 'html.parser')

        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
        print(csrf_token)
