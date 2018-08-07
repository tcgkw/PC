from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.stride_tricks import as_strided


######## K- means started############

def kmeans(data, k):
    clusterAssment = np.zeros(shape=(data.shape[0], 2))
    clusterAssment[:,0] = data      # input target dataset to clusterAssment, first column is GLV value, second column is cluster index
    cluster_changed = True
    centroids = [data.max(), data.min()]

    while cluster_changed:
        cluster_changed = False

        ## for each point in data
        for i in range(data.shape[0]):
            minDist = 10000.0
            min_index = 0

            ##  find the centroid which is the closest
            for j in range(k):
                distance = abs(data[i]-centroids[j])
                if distance < minDist:
                    minDist = distance
                    min_index = j

            if clusterAssment[i,1] != min_index:
                cluster_changed = True
                clusterAssment[i, 1] = min_index

        ## update new centroid after new cluster assigned
        for j in range(k):
            tag = np.where(clusterAssment[:,1] == j)[0]
            if len(tag) >0:
                s = 0
                for element in tag:
                    s += clusterAssment[element][0]
                centroids[j] = s / len(tag)

    # print('Congratulations, cluster complete!')
    return centroids, clusterAssment


######## K- means finished ############


# function below used to compress image for quicker calculation
def strided_rescale(g, bin_fac):
    strided = as_strided(g,
        shape=(g.shape[0]//bin_fac, g.shape[1]//bin_fac, bin_fac, bin_fac),
        strides=((g.strides[0]*bin_fac, g.strides[1]*bin_fac)+g.strides))
    return strided.mean(axis=-1).mean(axis=-1)
# function above used to compress image for quicker calculation

# function below is to detect edge and return edge type and edge px number
def detect_edge(path):
    original_img = np.array(Image.open(path).convert('L'), 'i')  # open target image
    ratio = int(original_img.shape[0] / 512)
    # ratio can be defined by user, now all images will be compressed to 512X512 px
    rescaled_image = np.flipud(np.uint8(strided_rescale(original_img, ratio)))

    # img = Image.fromarray(rescaled_image, 'L')  # transfer rescaled array to bmp for check purpose
    # img.save('E:\Python\Image boundary\\img.bmp')  # save rescaled image to bmp for check purpose

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
    # Finish to calculate both X and Y profile of image

    # Start to do K-means
    centroids, cluster1 = kmeans(x_profile, 2)
    centroids, cluster2 = kmeans(y_profile, 2)
    # K-means done

    cluster_x = cluster1[:, 1]
    cluster_y = cluster2[:, 1]

    x_diff_abs = np.absolute(np.diff(x_profile))
    y_diff_abs = np.absolute(np.diff(y_profile))

    x_peak = np.where(x_diff_abs > (x_diff_abs.mean() * 4))[0]  # 4 times larger than  mean is defined as a peak
    y_peak = np.where(y_diff_abs > (y_diff_abs.mean() * 4))[0]
    # find the edge of pattern by the  diff peak which  is closest to cluster with higher GLV
    edge_px_x = 0
    edge_px_y = 0
    # detect x direction edge and get edge px number
    if x_peak.size > 0:
        x_l = x_peak[0]
        x_r = x_peak[-1]
        if np.mean(cluster_x[:int(len(cluster_x) / 2)]) < np.mean(cluster_x[int(len(cluster_x) / 2):]):
            x_dir = 'right edge'
            edge_px_x = x_l * ratio
        elif np.mean(cluster_x[:int(len(cluster_x) / 2)]) > np.mean(cluster_x[int(len(cluster_x) / 2):]):
            x_dir = 'left edge'
            edge_px_x = x_r * ratio
        else:
            x_dir = 'X direction edge detection error!'
    else:
        x_dir = 'center'
    # detect x direction edge
    # detect y direction edge
    if y_peak.size > 0:
        y_b = y_peak[0]
        y_t = y_peak[-1]
        if np.mean(cluster_y[:int(len(cluster_y) / 2)]) < np.mean(cluster_y[int(len(cluster_y) / 2):]):
            y_dir = 'top edge'
            edge_px_y = y_b * ratio
        elif np.mean(cluster_y[:int(len(cluster_y) / 2)]) > np.mean(cluster_y[int(len(cluster_y) / 2):]):
            y_dir = 'bottom edge'
            edge_px_y = y_t * ratio
        else:
            y_dir = 'Y direction edge detection error!'
    else:
        y_dir = 'center'
    # detect y direction edge

    plt.plot(x_diff_abs)
    plt.xlabel('X_profile')
    plt.show()
    plt.plot(y_diff_abs)
    plt.xlabel('Y_profile')
    plt.show()
    return {'x_dir': x_dir, 'edge_px_x': edge_px_x, 'y_dir': y_dir, 'edge_px_y': edge_px_y}

path = 'E:\Python\Image boundary\\test images\\image-201-1-5-5-0.bmp'
result = detect_edge(path)
print(result)
# print(x_dir, '\n', edge_px_x, '\n', y_dir, '\n', edge_px_y)
