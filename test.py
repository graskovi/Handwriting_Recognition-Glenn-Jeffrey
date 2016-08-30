import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from skimage import img_as_ubyte
from skimage import data
from skimage.filters.rank import median, mean
from skimage.morphology import disk

"""hwrite = img_as_ubyte(Image.open('handwriting.jpg'))
#hist = np.histogram(noisy_image, bins=np.arange(0, 256))

#fig, (ax1) = plt.subplots(1, figsize=(8, 3))
#ax1 = ax1.ravel()
fig, ax = plt.subplots(2, 2, figsize=(10, 7), sharex=True, sharey=True)
print type(ax)
ax = ax.ravel()
print type(ax)

ax.imshow(hwrite, vmin=0, vmax=255, cmap=plt.cm.gray)
ax.set_title('Noisy')
ax.axis('off')
ax.set_adjustable('box-forced')

ax.imshow(median(hwrite, disk(1)), vmin=0, vmax=255, cmap=plt.cm.gray)
ax.set_title('Cleaner')
ax.axis('off')
ax.set_adjustable('box-forced')"""

noisy_image = img_as_ubyte(Image.open('handwriting.jpg'))

print noisy_image

#noisy_image.reshape()

new_im = Image.new('L', Image.open('handwriting.jpg').size)

for x in range(new_im.size[0]):
    for y in range(new_im.size[1]):
        new_im.putpixel((x,y), noisy_image)

new_im.show()

"""fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10, 7], sharex=True, sharey=True)

med = median(noisy_image, disk(2))

ax1.imshow(noisy_image, vmin=0, vmax=255, cmap=plt.cm.gray)
ax1.set_title('Original')
ax1.axis('off')
ax1.set_adjustable('box-forced')

ax2.imshow(med, vmin=0, vmax=255, cmap=plt.cm.gray)
ax2.set_title('Local mean $r=10$')
ax2.axis('off')
ax2.set_adjustable('box-forced')

plt.show()"""
