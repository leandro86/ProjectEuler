import time


def getCollatzSequenceLen(n, seqLenLookup):
    if n in seqLenLookup:
        return seqLenLookup[n]

    nextN = n // 2 if n % 2 == 0 else 3 * n + 1
    seqLenLookup[n] = getCollatzSequenceLen(nextN, seqLenLookup) + 1

    return seqLenLookup[n]


def solve():
    maxStartingNumber = 1000000

    seqLenLookup = {1: 1}
    bestStartingNumber = [0, 0]

    for i in range(1, maxStartingNumber):
        chainLen = getCollatzSequenceLen(i, seqLenLookup)
        if chainLen > bestStartingNumber[1]:
            bestStartingNumber[0] = i
            bestStartingNumber[1] = chainLen

    print("Number: {0}, Chain Length: {1}".format(bestStartingNumber[0], bestStartingNumber[1]))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)