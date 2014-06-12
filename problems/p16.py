import time


def solve():
    print(sum(int(i) for i in str(2 ** 1000)))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)