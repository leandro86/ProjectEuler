import time
from helpers import misc


def solve():
    primeFactors = misc.factorize(600851475143)
    print(max(primeFactors))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)
