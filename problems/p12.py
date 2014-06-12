import time
import functools
import operator

from helpers import misc


def getTriangleValue(n):
    return (n * (n + 1)) // 2


def countDivisors(n):
    primeFactors = misc.factorize(n)

    if len(primeFactors) > 0:
        # Given the prime factorization of a number n, for
        # instance: p^a q^b r^c, the number of divisors can be
        # computed as: (a+1)(b+1)(c+1). Given than 'primeFactors'
        # is a dictionary where: key --> prime factor, value --> multiplicity, it's
        # very easy to compute the number of divisors.
        return functools.reduce(operator.mul, map(lambda x: x + 1, primeFactors.values()))

    return 0


def solve():
    triangleNumber = 1
    triangleValue = getTriangleValue(triangleNumber)

    while countDivisors(triangleValue) <= 500:
        triangleNumber += 1
        triangleValue = getTriangleValue(triangleNumber)

    print("Triangle number: {0}, Value: {1}".format(triangleNumber, triangleValue))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)