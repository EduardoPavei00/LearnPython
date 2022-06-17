def number(y):
    sum = 0
    num_str = str(y)
    for x in range(len(num_str)):
        sum += int(num_str[x]) ** (x+1)
    if sum == y:
        print(sum, "---->", True)


def verification():
    for i in range(1000000):
        number(i)
    print("fim")


verification()