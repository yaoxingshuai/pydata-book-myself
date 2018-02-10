import numpy as np
import matplotlib.pyplot as plt

arr = np.empty((6, 3))
for i in range(len(arr)):
    arr[i] = i

print('筛选arr的第5，1，3行，构建新矩阵')
arr2 = arr[[5, 1, 3]]
arr2[1] = 6

print('修改新矩阵，src不变，因为是副本，而不是引用')
print(arr2, arr)

print('下面画个颜色代表数值的图，很牛逼')
arr = np.random.randn(6, 3)
plt.imshow(arr, cmap=plt.cm.Greens)
plt.colorbar()
plt.show()
