import numpy as np

data = np.random.randn(6, 3)
print(data)  # 6*3的矩阵，服从标准正态分布的数
print(data < 0)  # 6*3的矩阵，<0为True

print('将所有<0的数置0')
data[data < 0] = 0
print(data)

names = np.array(['hello', 'sky', 'hello', 'dan', 'hello', 'world'])
print('用names得到一个索引，筛选data')
print(names == 'hello')
data[names == 'hello'] = 9
print(data[0])
