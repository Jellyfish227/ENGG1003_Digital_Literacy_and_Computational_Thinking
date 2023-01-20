ordinal = ("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th")


def getUnitDigit(n: int):
    return n % 10


n = int(input("n?"))

for n in range(21, n + 1):
    print(n, ordinal[getUnitDigit(n)])
