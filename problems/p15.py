import time


def computeRoutesBottomUp(gridSize):
    memo = [[0] * (gridSize + 1) for i in range(gridSize + 1)]
    memo[gridSize][gridSize] = 1

    # All intersections in the last column and row would always be 1.
    for i in range(gridSize - 1, -1, -1):
        memo[gridSize][i] = 1
        memo[i][gridSize] = 1

    for y in range(gridSize - 1, -1, -1):
        for x in range(gridSize - 1, -1, -1):
            memo[y][x] = memo[y + 1][x] + memo[y][x + 1]

    return memo[0][0]


def computeRoutesTopDown(x, y, gridSize, memo):
    n = y * (gridSize + 1) + x

    if n not in memo:
        downPathsCount = 0
        rightPathsCount = 0

        if x < gridSize:
            rightPathsCount = computeRoutesTopDown(x + 1, y, gridSize, memo)

        if y < gridSize:
            downPathsCount = computeRoutesTopDown(x, y + 1, gridSize, memo)

        memo[n] = downPathsCount + rightPathsCount

    return memo[n]


def solve():
    gridSize = 20

    # A grid of size N has N + 1 intersections (both horizontal and vertical). So I need to
    # put a "1" in the lookup table in the last intersection of the grid.
    #print(computeRoutesTopDown(0, 0, gridSize, {(gridSize + 1) ** 2 - 1: 1}))

    print(computeRoutesBottomUp(gridSize))


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)