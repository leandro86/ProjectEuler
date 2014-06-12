import time


def solve():
    limit = 1000
    foundTriplet = False

    a = 1
    while not foundTriplet and a <= limit // 3:
        b = a + 1
        c = limit - a - b
        while not foundTriplet and c > b:
            if a * a + b * b == c * c:
                print("{{{0}, {1}, {2}}}. Product: {3}".format(a, b, c, a * b * c))
                foundTriplet = True
            else:
                b += 1
                c = limit - a - b
        a += 1


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)