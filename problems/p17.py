import time


# just trying to get the job done as quickly as possible, nothing fancy...
def numberToWords(n, words):
    if n < 20:
        return words[0][n]

    if n < 100:
        return words[1][n // 10] + "" + numberToWords(n % 10, words)

    if n < 1000:
        remainingWords = numberToWords(n % 100, words)
        return words[0][n // 100] + "hundred" + ("and" + remainingWords if remainingWords else "")

    return "onethousand"


def solve():
    words = [
        ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
        ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    ]

    totalLetters = 0

    for i in range(1, 1001):
        number = numberToWords(i, words)
        totalLetters += len(number)

    print(totalLetters)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)