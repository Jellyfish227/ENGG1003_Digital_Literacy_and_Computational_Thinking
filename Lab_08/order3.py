x = float(input('x?'))
y = float(input('y?'))
z = float(input('z?'))

if x < y < z:
    print("Increasing order", x, y, z)

elif x > y > z:
    print("Decreasing order", x, y, z)

else:
    print("Out of order", x, y, z)
