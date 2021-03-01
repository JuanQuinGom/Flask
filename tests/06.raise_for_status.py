import requests

try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.