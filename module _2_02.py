print('Ведите три целых числа: ')
first=(input('первое число: '))
second=(input('второе число: '))
third=(input('третье число: '))
if first == second == third:                                  # check first condition
    print('3')
elif first == second or first == third or second == third:    # check second condition
    print('2')
else :                                                        # rest conditions
    print('0')
