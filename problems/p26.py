import time


def findLengthRepeatingDecimals(denominator):
    remainder = 1
    remainders = []
    foundPeriodic = False

    # Keep multiplying the remainder by 10 and divide by the denominator.
    # If at some point the remainder repeats itself, then it means that the
    # denominator is a periodic decimal. Then, the length of this periodic value is
    # easy to calculate, given that I save in a list every remainder.
    while remainder != 0 and not foundPeriodic:
        if remainder in remainders:
            foundPeriodic = True
        else:
            remainders.append(remainder)
            remainder = (remainder * 10) % denominator

    return len(remainders) - remainders.index(remainder) if foundPeriodic else 0


def solve():
    limit = 1000
    longestCycle = [2, 0]

    for i in range(2, limit):
        cycleLength = findLengthRepeatingDecimals(i)

        if cycleLength > longestCycle[1]:
            longestCycle[0] = i
            longestCycle[1] = cycleLength

    print("Number: {0}, cycle length: {1}".format(longestCycle[0], longestCycle[1]))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)