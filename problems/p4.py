import time


def isPalindrome(n):
    number = str(n)
    return number == number[::-1]


def solve():
    upperLimit = 999
    lowerLimit = 100
    maxPalindrome = 0

    for i in range(upperLimit, lowerLimit, -1):
        j = i
        while j >= lowerLimit and i * j > maxPalindrome:
            n = i * j
            if isPalindrome(n):
                maxPalindrome = n
            j -= 1

    print(maxPalindrome)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)
