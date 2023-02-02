import qrcode
import cv2

img = qrcode.make("https://reffect.co.jp/react/react-router-6#React_Router")
img.save("qr.png")

img = cv2.imread("qr.png")
cv2.imshow("Image", img)
cv2.waitKey()