def keys(number):
    value = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                value += str(i) + str(j)
    return value

print('Input number: ')
print(keys(int(input())))