import re
import unidecode


def rotate_word(string):
    inverted_word = ""
    for i in range(len(string)):
        x = string[-i-1]
        inverted_word = inverted_word + x

    inverted_word = re.sub("\s", "", inverted_word)
    inverted_word = unidecode.unidecode(inverted_word)

    return inverted_word


def palindromo(z):
    word = test
    word = re.sub("\s", "", word)
    word = unidecode.unidecode(word)
    if z == word:
        print(True, "->", word, "=======", z)
    else:
        print(False, "->" , word, "----->", z)


test = "SOCORRAM ME SUBI NO ÔNIBUS EM MARROCOS" #não pode colocar ponto, nem virgula
palindromo(rotate_word(test))