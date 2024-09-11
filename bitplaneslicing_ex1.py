#Bitplane slicing
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:/IP/cameraman.tif',0)
b=[128,64,32,16,8,4,2,1]
for k in range(len(b)):
    img1=img&b[k]
    plt.tight_layout()
    plt.subplot(2,4,k+1),plt.imshow(img1,cmap='gray')
    plt.title(f'bitplane = {np.log2(b[k])}')
plt.show()