import time


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def solve():
    print(sum(int(d) for d in str(factorial(100))))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)