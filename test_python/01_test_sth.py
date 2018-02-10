import numpy as np
from numpy.random import randn, random

print(random(), randn())

print('randn返回标准正态分布')
rect = randn(2,3,4)
print(rect)  # 维数是2*3*4

print(rect.sum(), rect.size, len(rect))  # -4.79833555042 24 2

