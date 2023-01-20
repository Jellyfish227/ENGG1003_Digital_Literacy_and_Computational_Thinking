ordinal = ("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th")


def getUnitDigit(n: int):
    return n % 10


def getTensDigit(n: int):
    return (n // 10) % 10


n = int(input("n?"))

if getTensDigit(n) == 1:
    print(n, "th")
else:
    print(n, ordinal[getUnitDigit(n)])
