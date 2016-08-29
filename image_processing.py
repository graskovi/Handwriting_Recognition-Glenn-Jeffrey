#process images, open them and convert to b&w, partition them etc.

import cv2, numpy
from PIL import Image, ImageDraw
from scipy.ndimage.filters import rank_filter
from collections import defaultdict
import math, random, sys, os, json

hwrite = Image.open( "./Digits/2.jpg" )
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

def imB2W(im_digit):
    return blackAndWhite(im_digit, 100)

def makeSize(im):
    return im.resize((231,299))
    

"""def linePartition(im, (x1,y1), (x2,y2)):
    for """

"""blackAndWhite(hwrite, 700) #Sample threshold, will need to be dynamic"""
