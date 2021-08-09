'''
This is to detect and return the text
'''
def ocr(image):

    import pytesseract
    # Insert your pytesseract location here after installing
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    data = pytesseract.image_to_string(image, lang='eng',config='--psm 6')
    #print(data)
    return (data)
