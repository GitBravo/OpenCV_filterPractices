import cv2
import numpy as np
from matplotlib import pyplot as plt
def filter_image():
        img = cv2.imread('butterfly_g.bmp')
        plt.subplot(1, 2, 1),plt.imshow(img)

        gaussian = cv2.GaussianBlur(img, (9,9), 10.0)
        dst = cv2.addWeighted(img, 1.5, gaussian, -0.5, 0, img)
        
        plt.title('Original'),plt.xticks([]), plt.yticks([]), plt.subplot(1, 2, 2),plt.imshow(dst)
        plt.title('Unsharp Masking'),plt.xticks([]), plt.yticks([])
        plt.show()
if __name__ == "__main__" :
        filter_image()
