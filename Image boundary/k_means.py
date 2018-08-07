import numpy as np
import math
from numpy import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.stride_tricks import as_strided
from scipy import ndimage

# function below used to compress image for quicker calculation

def strided_rescale(g, bin_fac):
    strided = as_strided(g,
        shape=(g.shape[0]//bin_fac, g.shape[1]//bin_fac, bin_fac, bin_fac),
        strides=((g.strides[0]*bin_fac, g.strides[1]*bin_fac)+g.strides))
    return strided.mean(axis=-1).mean(axis=-1)

# function above used to compress image for quicker calculation

original_img = np.array(Image.open('E:\Python\Image boundary\\image-204-1-0-0-0.bmp').convert('L'), 'i')     # open target image
ratio = int(original_img.shape[0]/512)
# ratio can be defined by user, now all images will be compressed to 512X512 px
rescaled_image = np.flipud(np.uint8(strided_rescale(original_img, ratio)))

img = Image.fromarray(rescaled_image, 'L')                  # transfer rescaled array to bmp for check purpose
img.save('E:\Python\Image boundary\\img.bmp')     # save rescaled image to bmp for check purpose

# Start to calculate  profile of image

sum_x = np.zeros(shape=(rescaled_image.shape[1]), dtype=int)
sum_y = np.zeros(shape=(rescaled_image.shape[0]), dtype=int)

for c in range(rescaled_image.shape[0]):
    for r in range(rescaled_image.shape[1]):
        sum_x[c] += rescaled_image[r][c]

for r in range(rescaled_image.shape[1]):
    for c in range(rescaled_image.shape[0]):
        sum_y[r] += rescaled_image[r][c]

x_profile = sum_x / rescaled_image.shape[0]
y_profile = sum_y / rescaled_image.shape[1]




def kmeans(data, k):
    clusterAssment = np.zeros(shape=(data.shape[0], 2))
    clusterAssment[:,0] = data
    cluster_changed = True
    centroids = [data.max(), data.min()]
    # print(centroids, '\n', clusterAssment)

    while cluster_changed:
        cluster_changed = False

        ## for each point in data
        for i in range(data.shape[0]):
            # print(i)
            minDist = 10000.0
            min_index = 0

            ## for each centroid, find the centroid which is the closest
            for j in range(k):
                distance = abs(data[i]-centroids[j])
                if distance < minDist:
                    minDist = distance
                    min_index = j

            if clusterAssment[i,1] != min_index:
                cluster_changed = True
                clusterAssment[i, 1] = min_index

        for j in range(k):
            tag = np.where(clusterAssment[:,1] == j)[0]
            if len(tag) >0:
                s = 0
                for element in tag:
                    s += clusterAssment[element][0]
                centroids[j] = s / len(tag)

            # print(tag)

    print('Congratulations, cluster complete!')
    return centroids, clusterAssment


dataSet = y_profile
k = 2
# centroids, clusterAssment = kmeans(dataSet, k)
centroids, cluster = kmeans(dataSet, k)
# print(cluster)
cc= cluster[:,1]
ca = np.mean(cc[:int(len(cc)/2)])
ca2 = np.mean(cc[int(len(cc)/2):])
print(ca, ca2)
