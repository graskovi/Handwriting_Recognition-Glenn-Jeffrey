from PIL import Image
import random

hwrite = Image.open( "handwriting.jpg" )
black, white = (0,0,0), (255,255,255)

def blackAndWhite(im, thresh):
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            (r,g,b) = im.getpixel((x,y))
            if r+g+b <= thresh:
                im.putpixel((x,y), black)
            else:
                im.putpixel((x,y), white)
    im.show()

'''def linePartition(im, (x1,y1), (x2,y2)):
    for '''

blackAndWhite(hwrite, 700) #Sample threshold, will need to be dynamic
