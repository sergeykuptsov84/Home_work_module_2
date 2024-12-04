numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []          # 2, 3, 5, 7, 11, 13
not_primes = []      # 4, 6, 8, 9, 10, 12, 14, 15
for i in numbers:
    prime = True
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)