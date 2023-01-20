cards = ["Spade King", "Heart Ace", "Diamond Queen", "Club Jack"]
print("Initial: ", cards)

import random                # import module random
random.shuffle(cards)
print("First shuffle: ", cards)

from random import shuffle   # import function shuffle
shuffle(cards)
print("Second shuffle: ", cards)
