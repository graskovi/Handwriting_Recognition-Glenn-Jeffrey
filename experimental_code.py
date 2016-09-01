import numpy as np
from skimage.io import imread
from skimage.filters import threshold_otsu
from skimage.transform import resize
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage import restoration
from skimage import measure

def preprocess_image(im):
        """
        Denoises and increases contrast. 
        """
        im = imread(path, as_grey=True)
        image = restoration.denoise_tv_chambolle(im, weight=0.1)
        thresh = threshold_otsu(image)
        im_bw = closing(image > thresh, square(2))
        im = im_bw.copy()
        return im

def get_text_candidates(path):
    """identifies objects in the image. Gets contours, draws rectangles around them
    and saves the rectangles as individual images."""
    
    im_arr = imread(path, as_grey=True)
    
    label_image = measure.label(im_arr)   
    borders = np.logical_xor(preprocess_image(im_arr), im_arr)
    label_image[borders] = -1
    
    coordinates = []
    i=0
        
    for region in regionprops(label_image):
        if region.area > 10:
            minr, minc, maxr, maxc = region.bbox
            margin = 3
            minr, minc, maxr, maxc = minr-margin, minc-margin, maxr+margin, maxc+margin
            roi = self.image[minr:maxr, minc:maxc]
            if roi.shape[0]*roi.shape[1] == 0:
                continue
            else:
                if i==0:
                    samples = resize(roi, (28,28))
                    coordinates.append(region.bbox)
                    i+=1
                elif i==1:
                    roismall = resize(roi, (28,28))
                    samples = np.concatenate((samples[None,:,:], roismall[None,:,:]), axis=0)
                    coordinates.append(region.bbox)
                    i+=1
                else:
                    roismall = resize(roi, (28,28))
                    samples = np.concatenate((samples[:,:,:], roismall[None,:,:]), axis=0)
                    coordinates.append(region.bbox)
        
    candidates = {
                'fullscale': samples,          
                'flattened': samples.reshape((samples.shape[0], -1)),
                'coordinates': np.array(coordinates)
                }
        
    print 'Images After Contour Detection'
    print 'Fullscale: ', candidates['fullscale'].shape
    print 'Flattened: ', candidates['flattened'].shape
    print 'Contour Coordinates: ', candidates['coordinates'].shape
    print '============================================================'

    print candidates
    return candidates
