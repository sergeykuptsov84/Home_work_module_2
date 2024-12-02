# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# prime = True
# for i in range(2, 16):
#     for j in range(2, 9):
#         if i % j == 0:
#             break
#         print(i, 'is not prime number')
#     else:
#             print(i, "is a prime number")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
prime = True
for i in range(2, 16):
    for j in range(2, 9):
        if i % j == 0:
            break
        print(i, 'is not prime number')
    else:
            print(i, "is a prime number")
