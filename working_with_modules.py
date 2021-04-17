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

c = sys.path
print(c)


import threading as th

d = th.TIMEOUT_MAX
print(d)

# import all definition from a module. this is not advised as it can cause name colision
from math import *

e = pi
print(e)
