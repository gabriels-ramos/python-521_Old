import requests


#Consultar por ID
URL = 'https://gen-net.herokuapp.com/api/users/{}'
ID = input ('Digite ID do usuario: ')
URL_ID = URL.format(ID)
response = requests.get(URL_ID)
print(response.json())

print('--------------------------------------------------')

#Consultar por e-mail
URL = 'https://gen-net.herokuapp.com/api/users'

res = requests.get(URL)
users = res.json()

email = input('Digite seu email: ')

for user in users:
    if user.get('email') == email:
        print(user)

print('--------------------------------------------------')

#Teste sem variavel
print((requests.get('https://gen-net.herokuapp.com/api/users').json()))
