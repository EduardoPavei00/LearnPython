def convert(char: str):
    if char == 'a':
        return 'z'
    if char == 'b':
        return 'y'
    if char == 'c':
        return 'x'
    if char == 'd':
        return 'k'
    else:
        return "__"


def remove_char_duplicate(string: str):
    new_string = ""
    x = ""
    for i in string:
        if i != x:
            new_string += i
        else:
            new_string += ""
        x = i
    return new_string


print(remove_char_duplicate("aaaba"))


def translate(word: str):
    new_word = ""
    for i in word:
        translate_word = convert(i)
        new_word += translate_word

    remove_duplicate = remove_char_duplicate(new_word)
    return remove_duplicate


# print(translate("aabbbc"))