'''
exercicio 1

crie um programa que recebe como entrada dois numeros reais.
o programa deve imprimir as quatros operações matemáticas entre 
os dois números (soma, subtração, divisão e multiplicação).

'''

n1 = float(input('digite o primeiro numero: '))
n2 = float(input('digite o segundo numero: '))

resultado_soma = n1 + n2
print('soma: ', resultado_soma)

resultado_subtracao = n1 - n2
print('subtracao: ', resultado_subtracao)

resultado_multiplicacao = n1 * n2
print('multiplicacao: ', resultado_multiplicacao)

if n2 != 0:
    resultado_divisao = n1 / n2
    print('divisao: ', resultado_divisao)
else:
    print('Erro: divisao por zero')