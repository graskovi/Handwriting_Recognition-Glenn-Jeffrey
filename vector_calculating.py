#converts a black & white image to vector
#compares two vectors and returns similarity, assuming same dimensions

from PIL import Image
import PIL
import scipy.stats

#################################################################################

def vector(im):
    vect = []
    im = im.convert('1')
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            black = im.getpixel((x,y))==0
            vect.append(black)
    return vect

#################################################################################

def max_in_list(list):
    ind = 0
    maxInd = ind + 1
    maxFloat = maxInd
    while ind < len(list):
        if (list[ind] > list[maxInd]):
            maxInd = ind
            maxFloat = list[ind]
        ind += 1
    return maxFloat, maxInd

#################################################################################

def compare(data_vect, digit_vect):
    return scipy.stats.pearsonr(data_vect, digit_vect)[0]

#################################################################################

def findNum(path):
    '''returns the max pearsonr correlation coefficient and the associated digit'''
    
    vList = []
    
    vList.append(vector(Image.open("./Digits/0.jpg").resize((231,299),PIL.Image.ANTIALIAS)))
    vList.append(vector(Image.open("./Digits/1.jpg")))
    vList.append(vector(Image.open("./Digits/2.jpg")))
    vList.append(vector(Image.open("./Digits/3.jpg")))
    vList.append(vector(Image.open("./Digits/4.jpg")))
    vList.append(vector(Image.open("./Digits/5.jpg")))
    vList.append(vector(Image.open("./Digits/6.jpg")))
    vList.append(vector(Image.open("./Digits/7.jpg")))
    vList.append(vector(Image.open("./Digits/8.jpg")))
    vList.append(vector(Image.open("./Digits/9.jpg")))

    pcor = []

    imVect = vector(Image.open(path).resize((231, 299), PIL.Image.ANTIALIAS))

    for v in vList:
        pcor.append(compare(imVect, v))
        
    maxFloat, maxInd = max_in_list(pcor)
    
    return maxFloat, maxInd

#################################################################################

if __name__ == "__main__":

    maxFloat, maxInd = findNum('written8.jpeg')
    print 'The largest correlation is ', maxFloat, 'and', maxInd,'is the digit'
