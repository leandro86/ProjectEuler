import unittest
import itertools

from helpers import misc


class MiscTests(unittest.TestCase):
    def testFib(self):
        fibs = itertools.islice(misc.fib(), 10)

        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], list(fibs))

    def testFactorize(self):
        primeFactors = misc.factorize(16)

        self.assertEqual({2: 4}, primeFactors)

    def testFactorize2(self):
        primeFactors = misc.factorize(13195)

        self.assertEqual({5: 1, 7: 1, 13: 1, 29: 1}, primeFactors)

    def testPrimes(self):
        primes = itertools.islice(misc.primes(), 30)

        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                          43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                          101, 103, 107, 109, 113], list(primes))

    def testDivisors(self):
        divisors = misc.divisors(220)

        self.assertEqual([1, 2, 4, 11, 22, 44, 5, 10, 20, 55, 110, 220], divisors)


if __name__ == '__main__':
    unittest.main()
