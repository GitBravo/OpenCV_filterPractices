import cv2
import numpy as np
from matplotlib import pyplot as plt
def blur_image3():
        img = cv2.imread('butterfly_g_saltpepper_0.05.jpg')
        dst = cv2.medianBlur(img,5)
        plt.subplot(1, 2, 1),plt.imshow(img)
        plt.title('Original'),plt.xticks([]), plt.yticks([]), plt.subplot(1, 2, 2),plt.imshow(dst)
        plt.title('Blurred'),plt.xticks([]), plt.yticks([])
        plt.show()
if __name__ == "__main__" :
        blur_image3()
