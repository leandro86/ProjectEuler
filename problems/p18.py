import time
import os


# I choose to load the triangle as a list of numbers. For the triangle
#
#       3
#      7 4
#     2 4 6
#    8 5 9 3
#
# the list would be: [3, 7, 4, 2, 4, 6, 8, 5, 9, 3]
#
# Now, for a given number, to access the left and right numbers below, I need to
# keep track of the current level of the triangle and the index of the current number in the list.
# Then, to access the two numbers below, I would have to use a simple formula:
#
# index of left number below = index + level + 1
# index of right number below = index + level + 2
#
# For instance, given the number 6, its index in the list would be 5, and it's placed on level
# 2 of the triangle. So:
#
# index of left number below (9): index(5) + level(2) + 1 = 8
# index of right number below (3): index(5) + level(2) + 2 = 9
def loadTriangle():
    numbers = []

    with open(os.path.join("files", "triangle.txt")) as file:
        for line in file:
            numbers.extend([int(n) for n in line.strip().split(" ")])

    return numbers


# the triangle is small enough, no need to dynamic programming here, although
# it seems that it would be necessary in problem 67
def findMax(numbers, i, level):
    if i >= len(numbers):
        return 0

    left = findMax(numbers, i + level + 1, level + 1)
    right = findMax(numbers, i + level + 2, level + 1)

    return numbers[i] + max(left, right)


def solve():
    numbers = loadTriangle()
    print(findMax(numbers, 0, 0))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)