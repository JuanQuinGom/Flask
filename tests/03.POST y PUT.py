import requests 

response = requests.post('http://httpbin.org/post', data = {'key' : 'value'})

requests.put('https://httpbin.org/put', data = {'key' : 'value2'})