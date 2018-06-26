import cv2
import numpy as np
from matplotlib import pyplot as plt
def gradients_image():
        img = cv2.imread('butterfly_g.bmp',0)

        kernel_x = np.array([(-3, 0, +3), (-10, 0, +10), (-3, 0, +3)])
        kernel_y = np.array([(-3, -10, -3), (0, 0, 0), (+3, +10, +3)])

        sobelx= cv2.filter2D(img,cv2.CV_64F, kernel_x)
        sobely= cv2.filter2D(img,cv2.CV_64F, kernel_y)

        cv2.cartToPolar(sobelx, sobely, sobelx, sobely, 0)
        
        plt.subplot(2,2,1), plt.imshow(img,cmap= 'gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,3), plt.imshow(sobelx,cmap= 'gray')
        plt.title('Magnitude'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,4), plt.imshow(sobely,cmap= 'gray')
        plt.title('Orientation'), plt.xticks([]), plt.yticks([])
        plt.show()
if __name__ == "__main__" :
        gradients_image()
