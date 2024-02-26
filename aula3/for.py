#Estrutura de repetição
"""
utilizado para repetir uma instrução um determinado
número de vezes
"""

for x in range(1, 5):
    nome = input('digite o nome do aluno: \n')
    nota = float(input('digite a nota do aluno: \n'))
    if nota >= 6:
        print(nome," foi aprovado, com nota ", nota)
    else:
        print(f"{nome} foi reprovado com nota {nota: .2f}")