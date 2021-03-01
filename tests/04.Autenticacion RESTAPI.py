import requests

requests.get('https://api.github.com/user', auth=HTTPbasicAuth('username', 'password'))