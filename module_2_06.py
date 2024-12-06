a = input('Введите число: ')
b = int(a)
password = ''
for i in range(1, b):
    for j in range(i + 1, b):
        if b % (i + j) == 0:
            password += str(i) + str(j)
print('Ваш пароль:',password)
