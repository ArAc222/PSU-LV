import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('C:\\Users\\luka2\\PycharmProjects\\pythonProject\\HelloWorld\\tiger.png')
brig_img = img[:,:,0]
plt.figure()

#rotiranje
rotated_img = cv2.rotate(brig_img, cv2.ROTATE_90_CLOCKWISE)

#zrcaljenje
flipped_img = cv2.flip(brig_img,1)

#smanjivanje
shrinked_img = cv2.resize(brig_img, (0,0), fx=1, fy=0.1)


plt.subplot(1,5,1)
plt.imshow(brig_img)

plt.subplot(1,5,2)
plt.imshow(rotated_img)

plt.subplot(1,5,3)
plt.imshow(flipped_img)

plt.subplot(1,5,4)
plt.imshow(shrinked_img)

plt.show()
