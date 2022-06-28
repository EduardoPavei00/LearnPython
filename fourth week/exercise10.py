#Crie uma função que soma os respectivos elementos (números) de duas listas de igual tamanho.

def soma_list(list1, list2):
    new_list = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            x = list1[i] + list2[i]
            new_list.append(x)
    return new_list


print(soma_list([1, 4, 1], [2, 6, 2]))
