import numpy as np
from PIL import Image, ImageDraw
from skimage.io import imread
from skimage.filters import threshold_otsu
from matplotlib import pyplot as plt
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage import restoration
from skimage import measure
from skimage.color import label2rgb
import matplotlib.patches as mpatches

#################################################################################

class UserData():
    """class in charge of dealing with User Image input.
    the methods provided are finalized to process the image and return 
    the text contained in it."""

    def __init__(self, image_file):
        
        #reads the image provided by the user as grey scale and preprocesses it.
        
        self.image = imread(image_file, as_grey=True)
        self.preprocess_image()

#################################################################################

    def preprocess_image(self):
        '''Denoises and increases contrast.'''
        image = restoration.denoise_tv_chambolle(self.image, weight=0.1)
        thresh = threshold_otsu(image)
        self.bw = closing(image > thresh, square(2))
        self.cleared = self.bw.copy()
        return self.cleared

#################################################################################
    
    def plot_preprocessed_image(self):
        '''plots pre-processed image and returns crops of chars.'''

        rects = []
        
        image = restoration.denoise_tv_chambolle(self.image, weight=0.1)
        thresh = threshold_otsu(image)
        bw = closing(image > thresh, square(2))
        cleared = bw.copy()
        
        label_image = measure.label(cleared)
        borders = np.logical_xor(bw, cleared)
       
        label_image[borders] = -1
        image_label_overlay = label2rgb(label_image, image=image)
        
        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
        ax.imshow(image_label_overlay)
        
        for region in regionprops(label_image):
            if region.area < 10:
                continue
        
            minr, minc, maxr, maxc = region.bbox
            
            rects.append([minc, minr, maxc, maxr]) #EXTREMELY IMPORTANT LINE
            
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=2)
            ax.add_patch(rect)
        
        plt.show()

        return rects

#################################################################################

def get_chars(path):
    user = UserData(path)
    hwrite = Image.open(path)
    draw = ImageDraw.Draw(hwrite)
    rects = user.plot_preprocessed_image()
    chars = []
    for rect in rects:
        chars.append( hwrite.crop(tuple(rect)).resize((28,28),resample=Image.BICUBIC) )
    return chars

#################################################################################

if __name__ == '__main__':
    
    # creates instance of class and loads image    
    user = UserData('handwriting.jpg')
    
    # opens image and creates Class ImageDraw
    hwrite = Image.open('handwriting.jpg')
    draw = ImageDraw.Draw(hwrite)
    
    # plots preprocessed image and saves rectangles that contain chars in a list
    rects = user.plot_preprocessed_image()

    # creates list for images of chars
    chars = []

    # iterates through list of rects and draws them on PIL image
    for rect in rects:
            #draw.rectangle(rect, fill=None, outline='Black')
            chars.append( hwrite.crop(tuple(rect)).resize((100,100),resample=Image.BICUBIC) )

    # shows original image and image of sample cropped char
    hwrite.show()
    chars[0].show()
