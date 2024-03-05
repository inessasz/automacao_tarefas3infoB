'''
exercicio 2

crie um programa que recebe 2 números reais como entrada e um 
operador matemático. De acordo com o operador matemático fornecido
o programa apresentar o resultado da operação.
exemplo de entrada
1.2 
2.3
+
exemplo saída
o resultado da soma é 3.5
'''

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