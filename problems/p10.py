import time
import itertools

from helpers import misc


def solve():
    print(sum(itertools.takewhile(lambda x: x < 2000000, misc.primes())))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)