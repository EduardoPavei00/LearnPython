#Usando o while, implemente uma função que inverte uma lista dada como argumento,
# ou seja, o último elemento vira o primeiro da lista e vice-versa ([1,2,3] vira [3,2,1]).
# Não use lista[::-1], nem reverse().
import unittest


def inverte_list(number_list):
    i = 0
    new_list = []
    tamanho_string = len(number_list)
    while i < tamanho_string:
        new_list.append((tamanho_string - i)-(1))
        i = i + 1

    return new_list


class MyTest(unittest.TestCase):

    def test_empty_case(self):
        inverted = inverte_list([])
        print(inverted)
        self.assertEqual(inverted, [])

    def test_normal_case(self):
        original = list(range(4))
        inverted = inverte_list(list(range(4)))
        self.assertEqual(original,  list(range(4)))
        original.reverse()
        self.assertEqual(inverted,  original)





