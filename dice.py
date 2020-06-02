import random

def dice():
    return random.randint(1,7)

for i in range(2):
    print(dice())