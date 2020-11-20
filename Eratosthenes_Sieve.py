def sieve_eratosthenes(n):
    primes = []
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return primes

print(sieve_eratosthenes(121))
