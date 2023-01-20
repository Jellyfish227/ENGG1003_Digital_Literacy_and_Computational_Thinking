#!/usr/bin/env python3

# test interactively: exec(open("for_count_example.py").read())

N = int(input("Please enter N: "))

for i in range(1, N):
    print("Count", i)

print("Go!")


for i in range(1, N):
    print("Count", 10 + i * 2)

print("Go!")

