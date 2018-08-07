from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
# import edge_detection
import os



test =[1,2,3,4,5,6,]
a1 = np.asarray(test)
# print(test)
# plt.plot(np.diff(test))
#
# plt.show()

# print(np.any(a1 > 9 )  )

# test = {'x_dir': 'left', 'edge_px_x': 100, 'y_dir': 'center', 'edge_px_y': 200}


# test = [[1,2,3],[4,5,6],[7,8,9]]
# a = min(line[1] for line in test)
# print(a)
#
# path = 'E:\Python\Image boundary\\test images\\image-201-1-5-5-0.bmp'
# print(os.path.splitext(path))

for item in test:
    print (item)
    test.pop(item)
# print(test)