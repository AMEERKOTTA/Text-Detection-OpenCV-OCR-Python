# Text-Detection-OpenCV-OCR-Python
In this Repository, there is a Detailed Explanation of Text Detection from Images. Text Detection using OCR(Optical Character Recognition). Its Done by pytesseract Library. Text Detection Includes Character Detection, Word Detection, Digit Detection.
Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

**Python-tesseract** is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.

**Functions**
1. **get_tesseract_version** Returns the Tesseract version installed in the system
2. **image_to_string** Returns the result of a Tesseract OCR run on the image to string
3. **image_to_boxes** Returns result containing recognized characters and their box boundaries
4. **image_to_data** Returns result containing box boundaries, confidences, and other information
5. **image_to_osd** Returns result containing information about orientation and script detection
6. **image_to_alto_xml** Returns result in the form of Tesseract’s ALTO XML format
7. **run_and_get_output** Returns the raw output from Tesseract OCR. Gives a bit more control over the parameters that are sent to tesseract
