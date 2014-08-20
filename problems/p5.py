import time
from collections import defaultdict
from functools import reduce

from helpers import misc


def solve():
    # Brute force slow method
    maxDivisor = 20
    n = maxDivisor
    foundNumber = False

    while not foundNumber:
        divisor = 2
        while divisor <= maxDivisor and n % divisor == 0:
            divisor += 1

        if divisor > maxDivisor:
            foundNumber = True
        else:
            n += 20

    print(n)


def solve2():
    # A faster way using prime factorization
    maxFactor = 20
    factors = defaultdict(int)

    # This problem could be thought as finding the least common multiple
    # between the numbers 1..20. In order to do that, I calculate the prime
    # factors for the numbers 2..20. Then, I need to take all the prime
    # factors with the highest multiplicity and multiply them together.
    # I do here something similar: I keep track a dict with prime factors and
    # when a number has a prime factor with higher multiplicity than what already
    # is in the dict, I just add the prime factor as many times as the difference
    for factor in range(2, maxFactor + 1):
        primeFactors = misc.factorize(factor)
        for primeFactor, multiplicity in primeFactors:
            n = multiplicity - factors[primeFactor]
            if n > 0:
                factors[primeFactor] += n

    # At this points the dict could be something like this:
    # {2: 3, 3: 1, 5: 2}, where the key is the prime factor and
    # the value is the multiplicity. Now I need to raise the prime
    # factor to the power of the multiplicity, and then multiply all
    # the numbers. In this case would be:
    # 2^3 * 3^1 * 5^2
    print(reduce(lambda a, b: a * b, map(lambda x: x ** factors[x], factors)))


if __name__ == '__main__':
    startTime = time.time()
    #solve()
    solve2()
    print("Time elapsed: ", time.time() - startTime)