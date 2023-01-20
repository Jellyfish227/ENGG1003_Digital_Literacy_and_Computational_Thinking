print("Lucky Draw")

tickets = list( range(1, 100, 3) )  # create a new list
print("Original ticket numbers in ascending order:")
print(tickets)

import random
random.shuffle(tickets)
print("Shuffled ticket numbers in random order:")
print(tickets)

