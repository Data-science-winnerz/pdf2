'''
This contains methods to preprocess the images
Dilated image = no noise + thick font
eroded image = no noise +thin font
'''

import cv2
import numpy as np

# Converting to inverted image
def inverted(image):
    
    #inverted_image = cv2.bitwise_not(image)
    #cv2.imshow(image)
    #cv2.imwrite('inverted.png',inverted_image)
    return cv2.bitwise_not(image)

# Converting to gray scale
def grayscale(image):
    
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow(image)
    #cv2.imwrite('grayscale.png',inverted_image)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Conveting to black and white
def blackandwhite(image):
    image = np.array(image)
    thresh, im_bw = cv2.threshold(grayscale(image), 200, 230, cv2.THRESH_BINARY)
    
    #cv2.imshow("black and white",im_bw)
    #cv2.imwrite('bw.png',im_bw)
    #cv2.waitKey(0)
    return im_bw

# Removing noise
def noise_removal(image):
    import numpy as np
    kernal = np.ones((1,1), np.uint8)
    image = cv2.dilate(image, kernal, iterations=1)
    kernal = np.ones((1,1), np.uint8)
    image = cv2.erode(image, kernal, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernal)
    image = cv2.medianBlur(image, 3)
    
    #cv2.imshow(image)
    #cv2.imwrite('noise_removed.png',image)
    
    return (image)
    

# Converting to thin font
def thin_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernal = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernal, iterations=1)
    image = cv2.bitwise_not(image)
    
    #cv2.imshow(image)
    #cv2.imwrite('thin_font.png',image)
    
    return (image)

# Converting to thick font
def thick_font(image):
    import numpy as np
    image = cv2.bitwise_not(image)
    kernal = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernal, iterations=1)
    image = cv2.bitwise_not(image)

        
    #cv2.imshow(image)
    #cv2.imwrite('thick_font.png',image)

    return (image)
