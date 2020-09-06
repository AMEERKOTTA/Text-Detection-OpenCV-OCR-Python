import cv2
import pytesseract

## Python-tesseract is an optical character recognition (OCR) tool for python ##
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Fetch the image from respective Directory ##
image = cv2.imread("calc.png")
image = cv2.resize(image, (500,500))
## Convert image into RGB values from BGR ##
## pytesseract works good so ##
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))

## Detecting Words ##
heightImage,weightImage,_ = image.shape
boxes = pytesseract.image_to_data(image)
print(boxes)
## Forming bounding boxes around words ##
for x,b in enumerate(boxes.splitlines()):
    if x != 0:
       b = b.split()
       print(b)
       if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(image,(x,y),(w+x,h+y),(0,0,255),3)
            cv2.putText(image,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(20,30,255),2)


cv2.imshow("Detecting Words",image)
cv2.waitKey(0)