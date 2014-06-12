import itertools
import time

from helpers import misc


def solve():
    fibs = itertools.takewhile(lambda x: x < 4000000, misc.fib())
    print(sum(i for i in fibs if i % 2 == 0))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)
