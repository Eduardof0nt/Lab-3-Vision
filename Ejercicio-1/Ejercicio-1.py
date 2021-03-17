import matplotlib
import matplotlib.pyplot as plt

import skimage.filters
from skimage import io
import os

filename = os.getcwd() + '/Ejercicio-1/Img/Ejercicio1-b.jpeg'

image = io.imread(filename, as_gray=True)
imageOriginal = io.imread(filename, as_gray=False)

thresh = skimage.filters.threshold_otsu(image)
binary = image > thresh

fig, axes = plt.subplots(ncols=2, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(imageOriginal, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(binary, cmap=plt.cm.gray)
ax[1].set_title('Thresholded')
ax[1].axis('off')
plt.show()