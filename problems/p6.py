import time


def solve():
    n = 100

    sumOfSquares = sum([i * i for i in range(n + 1)])
    theSum = (n * (n + 1)) // 2

    print(theSum * theSum - sumOfSquares)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)