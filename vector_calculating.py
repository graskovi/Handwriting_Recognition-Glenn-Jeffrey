#
#

from PIL import Image
from image_processing import blackAndWhite as b2w
import scipy.stats

digit2 = Image.open("./Digits/2.jpg")
digit1 = Image.open("./Digits/1.jpg")

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
    (pcc, pval) = scipy.stats.pearsonr(data_vect, digit_vect)
    if (pval < 0.001):
        return sys.maxint
    return pcc/pval

if __name__ == "__main__":
    print scipy.stats.pearsonr(vector(digit2), vector(digit1))
