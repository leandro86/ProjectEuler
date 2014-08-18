import time

days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def isLeapYear(year):
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def daysInMonth(month, year):
    if month == 2 and isLeapYear(year):
        return 29
    return days[month - 1]


# This could be solved easily by using a date or calendar library, but of course that
# wouldn't be fun.
def solve():
    # Sum 1 to start at 1/1/1901.
    totalDays = sum((d for d in (daysInMonth(m, 1900) for m in range(1, 13)))) + 1

    # Careful! Need to check if 1/1/1901 was sunday before starting the loop.
    sundays = 1 if totalDays % 7 == 0 else 0

    for y in range(1901, 2001):
        for m in range(1, 13):
            totalDays += daysInMonth(m, y)
            if totalDays % 7 == 0:
                sundays += 1

    print(sundays)


if __name__ == "__main__":
    startTime = time.time()
    solve()
    print("Time elapsed: ", time.time() - startTime)