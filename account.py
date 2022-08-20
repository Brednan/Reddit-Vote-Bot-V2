from requests import Session
from bs4 import BeautifulSoup
from os import environ


class Account(Session):
    def __init__(self, username, password):
        self.SUCCESS = 1
        self.FAILED = 0

        Session.__init__(self)

        iproyal_username = environ['ip_royal_username']
        iproyal_password = environ['ip_royal_password']

        self.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'
        })

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

        form = {
            'csrf_token': csrf_token,
            'password': self.password,
            'dest': 'https://www.reddit.com',
            'username': self.username
        }

        res = self.post('https://www.reddit.com/login', timeout=5, data=form)

        res_json = res.json()

        try:
            if res_json['dest']:
                res_cookies = res.cookies

                loid = res_cookies.get('loid')

                self.headers.update({
                    'x-reddit-loid': loid
                })

                return self.SUCCESS

            else:
                return self.FAILED

        except KeyError:
            return self.FAILED

    def vote(self, comment_id, url):
        self.headers.update({
            'access-control-request-headers': 'authorization,x-reddit-loid,x-reddit-session',
            'access-control-request-method': 'POST'
        })

        vote_api_url = 'https://oauth.reddit.com/api/vote?redditWebClient=desktop2x&app=desktop2x-client-production&raw_json=1&gilding_detail=1'

        vote_options = self.options(vote_api_url, timeout=5)
