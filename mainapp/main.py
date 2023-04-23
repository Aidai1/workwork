import cv2
import qrcode


img = cv2.imread("frame.")
datect = cv2.QRCodeDetector()
result = datect.detectAndDecode(img)
print(result)





