import numpy as np
import unittest


def calcula_media_nota(notas, pesos):
    soma = 0
    media = np.multiply(notas, pesos)
    for h in range(len(media)):
        soma += media[h]
    return soma


def media_final(alunos, pesos=[0.3, 0.3, 0.4]):
    # if len(alunos.keys()) != len(pesos):
    #     raise Exception("different list size")
    dict_media = {}
    for i in alunos:
        notas_aluno = alunos.get(i)
        media_aluno = calcula_media_nota(notas_aluno, pesos)
        dict_media.update({i: media_aluno})

    return dict_media

d1 = {'eduardo': [7, 7, 7], 'joao': [7, 9, 8], 'pedro': [8, 8, 8]}


def boletin(alunos, pesos=[0.3, 0.3, 0.4]):

    for nome in alunos:
        notas = alunos[nome]
        media = 0
        i=0
        while i < len(notas):
            media += pesos[i]*notas[i]
            i+=1
        print("nome:", nome, "notas:", notas, "media:", int(media))




class Teste(unittest.TestCase):

    d1 = {'eduardo': [7, 7, 7], 'joao': [7, 9, 8], 'pedro': [8, 8, 8]}
    d2 = {'maria': [3.6, 3.3, 0, 7], 'joao': [7.9, 9.5, 8.1], 'pedro': [0.7, 5.8, 2.78]}
    d3 = {'eduardo': [7, 7, 7]}

    def test_calcula_media_notas(self):
        self.assertEqual(calcula_media_nota(self.d1['eduardo'], [0.3, 0.3, 0.4]), 7)
        self.assertAlmostEqual(calcula_media_nota([1, 10, 10], [0.333, 0.3333, 0.3333]), 7, delta=0.01)
        self.assertAlmostEqual(calcula_media_nota([10, 10, 4], [0, 0, 1]), 4, delta=0.01)

    def test_media_final(self):
        self.assertEqual(media_final(self.d1),  {'eduardo': 7, 'joao': 8, 'pedro': 8})


