import time
import os
import functools
import collections
import operator


def solve():
    with open(os.path.join("files", "1000_digit_number.txt")) as file:
        bigNumber = [int(digit) for digit in file.read()]

    maxProduct = 0

    # Simple bruteforce, although a few optimizations can be made
    for i in range(len(bigNumber) - 4):
        product = functools.reduce(operator.mul, bigNumber[i:i + 5])
        if product > maxProduct:
            maxProduct = product

    print(maxProduct)


def solve2():
    multiplyQueue = lambda q: functools.reduce(operator.mul, queue)

    # I start reading five numbers in a queue and calculate its product.
    # Then for every number read in the 1000 digit number, I dequeue one
    # digit (the digit on the left of the queue) and enqueue the new one.
    # There's no need to compute again the product of the digits in the
    # queue if the enqueued number is less or equal than the dequeued
    # one, since the queue's product will be equal or less than the
    # previous computed.
    # Also, if a read a 0, I need to clear the queue and start fillling
    # the queue again up to 5 digits.
    with open(os.path.join("files", "1000_digit_number.txt")) as file:
        queue = collections.deque(int(n) for n in file.read(5))
        maxProduct = multiplyQueue(queue)

        for n in file.read():
            if n == "0":
                queue.clear()
            else:
                if len(queue) == 5:
                    left = queue.popleft()

                newDigit = int(n)
                queue.append(newDigit)

                if len(queue) == 5 and newDigit > left:
                    maxProduct = max(maxProduct, multiplyQueue(queue))

    print(maxProduct)


if __name__ == "__main__":
    startTime = time.time()
    #solve()
    solve2()
    print("Time elapsed: ", time.time() - startTime)