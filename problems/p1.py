import time


def solve():
    print(sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)
