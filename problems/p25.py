import time
from helpers import misc


def solve():
    for i, f in enumerate(misc.fib()):
        if f >= 10 ** 999:
            print("{0}th -> {1}".format(i, f))
            break


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)