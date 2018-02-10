import pylab
from numpy.random import randn

# 两种plot的方式   pylab.plot   matplotlib.pyplot

img = pylab.imread('./imgs/autojump.png')
pylab.imshow(img)
pylab.show()

pylab.plot(randn(1000).cumsum())
pylab.plot(randn(1000))
pylab.show()


from matplotlib import pyplot as plt
from PIL import Image
img = Image.open('./imgs/autojump.png')
plt.imshow(img)
plt.show()

plt.plot(randn(1000).cumsum())
plt.show()
