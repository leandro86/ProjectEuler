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


def divisors(n):
    """
    Return a list with all divisors of n.
    """
    factors = factorize(n)
    divs = [1]

    for factor, multiplicity in factors.items():
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

