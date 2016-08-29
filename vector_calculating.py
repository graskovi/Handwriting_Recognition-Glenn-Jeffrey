#converts a black & white image to vector
#compares two vectors and returns similarity, assuming same dimensions

import matplotlib, cv2, numpy, hi
from PIL import Image
from image_processing import imB2W as b2w
from image_processing import makeSize
import scipy.stats

digitFirst = Image.open("./Digits/5.jpg")
digitSecond = Image.open("./Digits/6.jpg")

print type(digitFirst), type(digitSecond)

digitFirst = b2w(digitFirst)
digitSecond = b2w(digitSecond)

print type(digitFirst), type(digitSecond)

def vector(im):
    vect = []
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if type(im.getpixel((x,y))) == int:
                black = im.getpixel((x,y))==0
            else:
                (r,g,b) = im.getpixel((x,y))
                black = r+g+b==0
            vect.append(black)
    return vect

def compare(data_vect, digit_vect):
    return scipy.stats.pearsonr(data_vect, digit_vect)[0]

if __name__ == "__main__":
    print scipy.stats.pearsonr(vector(digitFirst), vector(digitSecond))
    print compare(vector(digitFirst), vector(digitSecond))
