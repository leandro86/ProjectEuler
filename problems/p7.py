import time
import itertools

from helpers import misc


def solve():
    print(next(itertools.islice(misc.primes(), 10000, None)))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)