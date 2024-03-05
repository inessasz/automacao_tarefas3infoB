'''
exercicio 3 

crie um programa que execute repetidamente o programa do
exercicio 2. Após a apresentação do resultado o programa deve
perguntar se o usuário deseja continuar a calcular, se a resposta
for S (sim) o programa deve continuar se a resposta for N (não)
o programa deve terminar.
'''
while True:
n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))
operador = input('digite um operador matemático(+, -, *, /): ')

if operador == '+': 
    resultado_soma = n1 + n2
    print('soma: ', resultado_soma)

elif operador == '-': 
    resultado_subtracao = n1 - n2
    print('subtracao: ', resultado_subtracao)

elif operador == '*': 
    resultado_multiplicacao = n1 * n2
    print('multiplicacao: ', resultado_multiplicacao)

else :
    resultado_divisao = n1 / n2
    print('divisao: ', resultado_divisao)


    continuar = input('deseja continuar? (S/N): ')
    if continuar.upper()  != 'S': 

   
