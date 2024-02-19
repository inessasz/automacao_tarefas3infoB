print('digite sua idade: ')
idade = int(input())


if idade <= 12:
    print('Você é uma criança')
elif idade < 18:
    print('você é um adolescente')
elif idade < 65:
    print('você é um adulto')
else: 
    print('você é um idoso')

idade = int(idade) + 1
print("No ano que vem sua idade será ", idade)
