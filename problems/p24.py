import time
import itertools


def findPermutations(a, b):
    if b == "":
        yield a

    for i in range(0, len(b)):
        yield from findPermutations(a + b[i], b[:i] + b[i + 1:])


def solve():
    permutations = findPermutations("", "0123456789")
    print(next(itertools.islice(permutations, 1000001, 1000002)))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)