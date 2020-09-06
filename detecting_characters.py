import cv2
import pytesseract

## Python-tesseract is an optical character recognition (OCR) tool for python ##
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Fetch the image from respective Directory ##
image = cv2.imread("calc.png")
image = cv2.resize(image,(450,450))
## Convert image into RGB values from BGR ##
## pytesseract works good so ##
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(image))



## Detecting Characters ##
heightImage,weightImage,_ = image.shape
boxes = pytesseract.image_to_boxes(image)
## Forming bounding boxes ##
for b in boxes.splitlines():
    # print(b)
    b = b.split(" ")
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(image,(x,heightImage-y),(w,heightImage-h),(0,0,255),3)
    cv2.putText(image,b[0],(x,heightImage-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(20,30,255),2)

cv2.imshow("Detecting Chracters",image)
cv2.waitKey(0)
