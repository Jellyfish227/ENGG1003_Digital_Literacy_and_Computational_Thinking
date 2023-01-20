sentence = "This is a GOOD day"
print("lower:", sentence.lower())
print("upper:", sentence.upper())
print("capitalize:", sentence.capitalize())
print("swapcase:", sentence.swapcase())
pieces = sentence.lower().split()
print("Broken into pieces:", pieces)
for word in pieces:
    print( word )

