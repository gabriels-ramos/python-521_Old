import requests

DOMAIN_URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite seu id: ')
name = input('Digite  seu nome: ')
email = input('Digite seu email: ')
password = input('DIgite sua senha: ')

payload = {
    'name': name,
    'email': email,
    'password': password
}

response = requests.put(DOMAIN_URL.format(user_id), payload)

if response.status_code == 200:
    print('Usuario atualizado com sucesso')
else:
    print('Erro ao atualizar o usuario')

print(response.status_code)