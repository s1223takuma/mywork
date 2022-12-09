import qrcode
import cv2

img = qrcode.make("https://github.com/")
img.save("qr.png")

img = cv2.imread("qr.png")
cv2.imshow("Image", img)
cv2.waitKey()