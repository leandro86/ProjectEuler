import time
from helpers import misc


def abundantNumbersBelow(n):
    abundantNumbers = set()

    for i in range(1, n):
        if sum(misc.divisors(i)[:-1]) > i:
            abundantNumbers.add(i)

    return abundantNumbers


def isSumOfTwoAbundants(n, abundantNumbers):
    for abundantNumber in abundantNumbers:
        if abundantNumber > n:
            return False
        if (n - abundantNumber) in abundantNumbers:
            return True


def solve():
    limit = 28123
    abundantNumbers = abundantNumbersBelow(limit + 1)
    theSum = 0

    for i in range(1, limit + 1):
        if not isSumOfTwoAbundants(i, abundantNumbers):
            theSum += i

    print(theSum)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)