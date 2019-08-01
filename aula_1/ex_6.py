import requests

DOMAIN_URL =  'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite id: ')

res = requests.put(DOMAIN_URL.format(user_id))

if res.status_code == 200:
    print(res.json().get('name'))
else:
    print(res.text)