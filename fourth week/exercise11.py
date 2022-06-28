# Implemente uma rotina que exibe os elementos de uma lista qualquer,
# considerando que os elementos dessa lista podem ser uma outra lista. Por exemplo:
#
# lista = [1,2, [3,4, [5]], 'controle', 6]
#
# A exibição se dará como abaixo:
# 1
# 2
# 3
# 4
# 5
# controle
# 6
#
# Dica: pode usar recursão, ou seja, a rotina chamar a ela mesma. Lembre-se que é possível testar se uma variável v tem tipo lista (type(v) == list).


def return_element(lista):
    for i in range(len(lista)):
        print(lista[i])


def teste(v):
    if type(v) == list:
        return_element(v)


list_number = [1,2, [3,4, [5]], 'controle', 6]
teste(list_number)