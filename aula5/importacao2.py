#importar so uma funcao do arquivo

from funcoes import login

while True: 
    user = input('digite o nome do usuário:')
    pwd = input('digite a senha do usuário;')
    if login(user, pwd):
        print('logado com sucesso')
        break
    else:
        print('tente novamente!')