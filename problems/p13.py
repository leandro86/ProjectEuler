import time
import os


def solve():
    with open(os.path.join("files", "50digits_numbers.txt")) as file:
        # The first two 50-digits numbers of the file are:
        #
        # 37107287533 902102798797998220837590246510135740250
        # 46376937677 490009712648124896970078050417018260538
        #
        # The problem asks for the first 10 digits of the
        # sum of all numbers.
        #
        # Looking at these first two numbers, I only need to
        # take the first 11 digits and compute the sum, since
        # the 12th digits (9 and 4) doesn't affect the result
        # of the first ten 10 digits.
        numbersSum = sum((int(line[:11]) for line in file))

    print(str(numbersSum)[:10])


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)