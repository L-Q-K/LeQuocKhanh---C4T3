from math import *
from time import *

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
    }
stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
    }

fruits = prices.keys()

total = {}
for fruit in fruits:
    print(fruit)
    print("price:", prices[fruit])
    print("stock:", stocks[fruit])
    total[fruit] = prices[fruit] * stocks[fruit]
    print()

for fruit in fruits:
    print("If i sell all my", fruit, ", i will have", total[fruit])

print(sum(list(total.values())))

sleep(3)

