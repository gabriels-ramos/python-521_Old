import requests

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users'

payload = {
    'name': input('Digite seu nome: '),
    'email': input('Digite seu email: '),
    'password': input('Digite seu password: ')
}

res = requests.post(DOMAIN_URL, payload)

if res.status_code == 200:
    user_id = res.json().get('id')
    print('Usuario {} cadastrado com sucesso'.format(user_id))
else:
    print('Email já cadastrado')