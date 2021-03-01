import requests 
try:
    response = requests.get('http://api.open-notify.org/astros.json') 
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)