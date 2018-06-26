import cv2
import numpy as np
from matplotlib import pyplot as plt
def filter_image():
        img = cv2.imread('butterfly_g.bmp')
        kernel = np.array([(-1, -1, -1), (-1, 8, -1), (-1, -1, -1)], np.float32)/9
        dst = cv2.filter2D(img,-1,kernel)
        plt.subplot(1, 2, 1),plt.imshow(img)
        plt.title('Original'),plt.xticks([]), plt.yticks([]), plt.subplot(1, 2, 2),plt.imshow(dst)
        plt.title('High-Pass Filter'),plt.xticks([]), plt.yticks([])
        plt.show()
if __name__ == "__main__" :
        filter_image()
