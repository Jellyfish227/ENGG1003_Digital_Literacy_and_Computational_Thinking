import math
import random
from typing import List, Tuple

fruits = ["Apple", "Orange", "Banana"]
print(fruits)

fruits.append("Durain")
print(fruits)

random.shuffle(
    fruits
)
print(fruits)

l = []
l = list(range(100))
print(l)

test = {"apple":"a red fruit", "car":"a vehical"}

print("")

k: str
for k in test.keys():
    print(k)

for v in test.values():
    print(v)

for k,v in test.items():
    print(k,v)


print("v is {}".format(v))