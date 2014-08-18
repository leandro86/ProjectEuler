import time
import os


def solve():
    with open(os.path.join("files", "names.txt")) as file:
        names = file.readline().replace('"', "").split(",")

    names.sort()

    totalScore = 0

    for i, name in enumerate(names):
        namePos = i + 1
        nameSum = 0

        for c in name:
            nameSum += ord(c) - ord("A") + 1

        totalScore += nameSum * namePos

    print(totalScore)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)