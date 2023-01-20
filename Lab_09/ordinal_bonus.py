n = int(input("n?"))


def getDigit(n: int, i: int):
    return (abs(n) // 10**(3-i)) % 10


ordinal = ("th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th")

for i in range(0,4):
    print(getDigit(n, i))

if n < 0:
    print(n, "is negative")

elif getDigit(n, 2) == 1:
    print("{0}{1}".format(n,"th"))
else:
    print("{0}{1}".format(n,ordinal[getDigit(n,3)]))
