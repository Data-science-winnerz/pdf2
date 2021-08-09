"""
This module is for converting the pdf to png and handle any rotation detection
"""

# This method is used to convert the pdf
def convo(path):
    from pdf2image import convert_from_path
    
    images = convert_from_path(path,dpi= 500, poppler_path=r'C:\Program Files\poppler-21.03.0\Library\bin')
    # images[0].save("sample.png",format = "PNG")
    
    return images[0]



def rotimage(image):
    import cv2
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt

    # load image as HSV and select saturation
    img = image
    hh, ww, cc = img.shape

    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold the grayscale image
    ret, thresh = cv2.threshold(gray,0,255,0)

    # find outer contour
    cntrs = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(cntrs)
    cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]
    

    # get rotated rectangle from outer contour
    rotrect = cv2.minAreaRect(cntrs[0])
    box = cv2.boxPoints(rotrect)
    box = np.int0(box)

    # draw rotated rectangle on copy orff img as result
    result = img.copy()
    cv2.drawContours(result,[box],0)

    # get angle from rotated rectangle
    angle = rotrect[-1]

    # from https://www.pyimagesearch.com/2017/02/20/text-skew-correction-opencv-python/
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)
    
    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = angle

    print(angle,"deg")

    cv2.imshow("THRESH", thresh)
    image = Image.fromarray(result)
    result = image.rotate(angle)
    plt.imshow(result)
    # result.save('out1.png')



def rot2(image):
    import cv2 as cv
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Load the image
    img = image
    
    # Convert image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # Convert image to binary
    _, bw = cv.threshold(gray, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    # Find all the contours in the thresholded image
    contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    angle = 0
    for i, c in enumerate(contours):
    
        # Calculate the area of each contour
        area = cv.contourArea(c)
        
        # Ignore contours that are too small or too large
        if area < 3700 or 100000 < area:
            continue
        
        # cv.minAreaRect returns:
        # (center(x, y), (width, height), angle of rotation) = cv2.minAreaRect(c)
        rect = cv.minAreaRect(c)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        
        # Retrieve the key parameters of the rotated bounding box
        center = (int(rect[1][1]),int(rect[1][1])) 
        width = int(rect[1][1])
        height = int(rect[1][1])
        angle = int(rect[2])
        
            
        if width < height:
            angle = 90 - angle
        else:
            angle = angle
                
        
    final = Image.fromarray(img)
    final = final.rotate(angle=angle)
    plt.imshow(final)
    
    # Save the output image to the current directory
    #cv.imwrite("min_area_rec_output.jpg", img)



