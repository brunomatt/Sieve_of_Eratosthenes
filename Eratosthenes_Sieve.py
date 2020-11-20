def prime_eratosthenes(n):
    composites = []
    primes = []
    for i in range(2, n+1):
        if i not in composites:
            primes.append(i)
            for j in range(i*i, n+1, i):
                composites.append(j)

    print(primes)