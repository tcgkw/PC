from PIL import ImageFilter
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.stride_tricks import as_strided
# im1 = Image.open('C:\Users\kgao\Documents\HMI\PyCharm\Image boundary\image-201-1-6-6-0.bmp')
# im2 = im1.filter(ImageFilter.FIND_EDGES)
#
# im2.save('C:\Users\kgao\Documents\HMI\PyCharm\Image boundary\\new.bmp')

# im3 = np.array(Image.open('image-201-1-6-6-0.bmp'))
# print(im3.shape, im3.dtype)

im4 = np.array(Image.open('image-201-1-6-6-0.bmp').convert('L'), dtype=np.uint8)                #convert image to numpy array, x and y index are pixel coordinate and value is gray level value
# print(im4.shape, type(im4.shape), im4.shape[0], type( im4.shape[0]))
sum = np.zeros(shape=(1, im4.shape[1]), dtype=int)                #1D array to store gray level value of each column


# # Start to calculate vertical profile of image
# for c in range(im4.shape[0]):
#     for r in range(im4.shape[1]):
#         sum[0][c] += im4[r][c]
#
# y_profile = sum / im4.shape[0]
# print(y_profile.min(), y_profile.argmin())
# # Finish to calculate vertical profile of image


# fig = plt.gcf()
# plt.hist(y_profile)
# plt.axis([0, 8192, 0, 255])
# plt.show()

def strided_rescale(g, bin_fac):
    strided = as_strided(g,
        shape=(g.shape[0]//bin_fac, g.shape[1]//bin_fac, bin_fac, bin_fac),
        strides=((g.strides[0]*bin_fac, g.strides[1]*bin_fac)+g.strides))
    return strided.mean(axis=-1).mean(axis=-1)  # order is NOT important! See notes..

rescale = np.uint8(strided_rescale(im4, 16))
img = Image.fromarray(rescale, 'L')
img.save('C:\Users\kgao\Documents\HMI\PyCharm\Image boundary\\img.bmp')
# img.show()

