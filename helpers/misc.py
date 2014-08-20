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

    Return a list of tuples (a,b) where: a -> factor, b -> multiplicity.
    """
    primeFactors = []

    i = 0
    while n % 2 == 0:
        i += 1
        n //= 2

    if i != 0:
        primeFactors.append((2, i))

    divisor = 3
    while divisor * divisor <= n:
        i = 0

        while n % divisor == 0:
            i += 1
            n //= divisor

        if i != 0:
            primeFactors.append((divisor, i))

        divisor += 2

    if n > 1:
        primeFactors.append((n, 1))

    return primeFactors


def divisors(n):
    """
    Return a list with all divisors of n.
    """
    factors = factorize(n)
    divs = [1]

    for factor, multiplicity in factors:
        moreDivs = []
        for i in range(1, multiplicity + 1):
            n = factor ** i
            for d in divs:
                moreDivs.append(n * d)
        divs.extend(moreDivs)

    return divs


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

            del (composites[n])

        n += 1

