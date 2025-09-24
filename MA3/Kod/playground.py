import random
from matplotlib import pyplot as plt
import numpy as np
import math as m

n = 10
nps = 3
print(n//nps)
print(n//nps*(nps-1))
print(n//nps + n%nps)
print(n//nps*(nps-1) + n//nps + n%nps)

sizes = [n//nps]*(nps-1) + [n//nps + n%nps]
print(sizes)