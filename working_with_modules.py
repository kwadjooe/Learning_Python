# help('modules') # loads all available modules in pyton

import math, random, sys

a = math.sqrt(4)
print(a)
lf = dir(math)
for l in lf:
    print(l)

# import random

b = random.randint(1, 1000)
print(b)

import threading as th

c = sys.path
print(c)
