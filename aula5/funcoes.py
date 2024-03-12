'''
as funções são utilizadas para modularizar o código, ou seja, 
dividi-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def nome_funcao(param1, param2):
    faz algo
    return valor

Exemplos:
'''
#função1
def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area
#função2
def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False 
    
#chamar a função
#print(login("admin", '123'))
#area = calcularAreaTriangulo(100, 50)
#print('a área do triângulo é:', area)
