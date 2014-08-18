import time
from helpers import misc


def solve():
    amicableNumbers = set()

    for a in range(10000):
        b = sum(misc.divisors(a)[:-1])
        db = sum(misc.divisors(b)[:-1])

        if db == a and a != b:
            amicableNumbers.add(a)
            amicableNumbers.add(b)

    print(sum(amicableNumbers))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)