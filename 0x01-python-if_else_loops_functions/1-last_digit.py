#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
dig = abs(num) % 10
if num < 0:
    dig = -dig
print("Last digit of {} is {} and is ".format(num, dig), end="")
if dig > 5:
    print("greater than 5")
elif dig == 0:
    print("0")
else:
    print("less than 6 and not 0")
