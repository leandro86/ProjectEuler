import time
import os
import functools
import operator


def solve():
    with open(os.path.join("files", "20x20_grid.txt")) as file:
        grid = []
        for line in file:
            numbers = [int(n) for n in line.split(" ")]
            grid.append(numbers)

    computeProduct = lambda x: functools.reduce(operator.mul, x)

    ADJ_NUMBERS = 4

    rows = len(grid)
    columns = len(grid[0])
    maxProduct = 0

    # Quick and relatively dirty way to solve it.
    # For each number in the grid, I compute all the
    # products: horizontal, vertical, dialognal left and diagonal right.
    for rowNumber, row in enumerate(grid):
        for i in range(rows):
            colChecked = False
            rowChecked = False

            if i < columns - (ADJ_NUMBERS - 1):
                # Horizontal product
                maxProduct = max(maxProduct, computeProduct(row[i:i + ADJ_NUMBERS]))
                colChecked = True

            # I can't do a multi axis slice in a list. I could've used a numpy
            # array here
            if rowNumber < rows - (ADJ_NUMBERS - 1):
                # Vertical product
                maxProduct = max(maxProduct, (computeProduct((grid[rowNumber][i],
                                                              grid[rowNumber + 1][i],
                                                              grid[rowNumber + 2][i],
                                                              grid[rowNumber + 3][i]))))
                rowChecked = True

            if rowChecked and colChecked:
                # Diagonal right product
                maxProduct = max(maxProduct, (computeProduct((grid[rowNumber][i],
                                                              grid[rowNumber + 1][i + 1],
                                                              grid[rowNumber + 2][i + 2],
                                                              grid[rowNumber + 3][i + 3]))))

            if rowChecked and i >= ADJ_NUMBERS - 1:
                # Diagonal left product
                maxProduct = max(maxProduct, (computeProduct((grid[rowNumber][i],
                                                              grid[rowNumber + 1][i - 1],
                                                              grid[rowNumber + 2][i - 2],
                                                              grid[rowNumber + 3][i - 3]))))

    print(maxProduct)

if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)