'''

para utilizarmos as funções criadas em outros
arquivos de código fonte devemos importa-las. para
isso utilizamos o comando import ou from import

Exemplo 1: importar todas as funções do arquivo
funções
'''
import funcoes

base = float(input('digite a base do triângulo: '))
altura = float(input('digite a altura do triângulo: '))

area = funcoes.calcularareaTriangulo(base, altura)
print(area)