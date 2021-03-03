import requests
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
    # Code here will only run if the request is successful
except requests.Timeout as error:
    print(error)