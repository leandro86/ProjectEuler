from collections import defaultdict


def fib():
    """
    Generate an infinite sequence of fibonacci numbers.
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def factorize(n):
    """
    Factorize 'n' and return its prime factors.

    Return a dictionary where: key --> prime factor, value --> multiplicity.
    """
    primeFactors = defaultdict(int)
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            primeFactors[divisor] += 1
            n //= divisor
        else:
            divisor += 1

    return primeFactors


def primes():
    """
    Generate an infinite sequence of prime numbers.
    """
    composites = {}
    n = 2

    while True:
        if n not in composites:
            yield n
            composites[n * n] = [n]
        else:
            for p in composites[n]:
                composites.setdefault(n + p, []).append(p)

            del(composites[n])

        n += 1

