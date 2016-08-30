#process images, open them and convert to b&w, partition them etc.

import cv2, numpy, math, random, sys, os, json
from numpy import ubyte
import matplotlib.pyplot as plt
from scipy.ndimage.morphology import binary_dilation as bindil
from PIL import Image, ImageDraw
#import ImageEnhance
#import ImageFilter
from scipy.ndimage.filters import rank_filter
from skimage import img_as_ubyte
from skimage.filters.rank import median
from skimage.morphology import disk
from collections import defaultdict

hwrite = Image.open( "handwriting.jpg" )
black, white = (0,0,0), (255,255,255)

def blackAndWhite(im, thresh):
    if type(im.getpixel((0,0))) == int:
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if im.getpixel((x,y)) <= thresh/3:
                    im.putpixel((x,y), 0)
                else:
                    im.putpixel((x,y), 255)
    else:
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                (r,g,b) = im.getpixel((x,y))
                if r+g+b <= thresh:
                    im.putpixel((x,y), black)
                else:
                    im.putpixel((x,y), white)
    return im
    """im = im.convert('1')
    im.show()"""

def imB2W(im_digit):
    return blackAndWhite(im_digit, 100)

def makeSize(im):
    return im.resize((231,299))

"""def removeNoise(im):
    noisy_image = img_as_ubyte(im)
    hist = numpy.histogram(noisy_image, bins=numpy.arange(0, 256))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
    ax1.imshow(noisy_image, interpolation='nearest', cmap=plt.cm.gray)
    ax1.axis('off')
    ax2.plot(hist[1][:-1], hist[0], lw=2)
    ax2.set_title('Histogram of grey values')
    
    noise = numpy.random.random(noisy_image.shape)
    #noisy_image = img_as_ubyte(noisy_image)
    noisy_image[noise > 0.99] = 255
    noisy_image[noise < 0.01] = 0

    fig, ax = plt.subplots(2, 2, figsize=(10, 7), sharex=True, sharey=True)
    ax1, ax2, ax3, ax4 = ax.ravel()

    ax1.imshow(noisy_image, vmin=0, vmax=255, cmap=plt.cm.gray)
    ax1.set_title('Noisy image')
    ax1.axis('off')
    ax1.set_adjustable('box-forced')

    ax2.imshow(median(noisy_image, disk(1)), vmin=0, vmax=255, cmap=plt.cm.gray)
    ax2.set_title('Median $r=1$')
    ax2.axis('off')
    ax2.set_adjustable('box-forced')


    ax3.imshow(median(noisy_image, disk(5)), vmin=0, vmax=255, cmap=plt.cm.gray)
    ax3.set_title('Median $r=5$')
    ax3.axis('off')
    ax3.set_adjustable('box-forced')


    ax4.imshow(median(noisy_image, disk(20)), vmin=0, vmax=255, cmap=plt.cm.gray)
    ax4.set_title('Median $r=20$')
    ax4.axis('off')
    ax4.set_adjustable('box-forced')"""

def clean(im):
    im = img_as_ubyte(im)
    im = median(im, disk(1))
    im.show()

def arr2img(ar):
    #Convert Numeric array to PIL Image
    return Image.frombytes('L', (ar.shape[1], ar.shape[0]), ar.astype(ubyte).tostring())

def arr2PIL(arr, size):
    mode = 'RGBA'
    arr = arr.reshape(arr.shape[0]*arr.shape[1], arr.shape[2])
    if len(arr[0]) == 3:
        arr = numpy.c_[arr, 255*numpy.ones((len(arr),1), numpy.uint8)]
    return Image.frombuffer(mode, size, arr.tostring(), 'raw', mode, 0, 1)

def dilate(im):
    #im = blackAndWhite(im, 650)
    image = cv2.imread(str(im.convert('1')), 0)
    kernel = numpy.ones((5,5),numpy.uint8)
    new_image = cv2.dilate(image,kernel,iterations=1)
    #print type(new_image)
    new_image = arr2PIL(new_image)
    new_image.show()


if __name__ == "__main__":
    dilate(hwrite)
    #blackAndWhite(hwrite, 650)
