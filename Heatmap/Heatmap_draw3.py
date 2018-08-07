import numpy as np
import re
import matplotlib.pyplot as plt


x_period = 880
y_period = 880
sum = np.zeros(shape=((int(29499/y_period)+1), (int(48426/x_period))+1), dtype=float)
count = np.zeros(shape=((int(29499/y_period)+1), (int(48426/x_period))+1), dtype=int)

with open('Y:\Python\Heat map\\temp\\temp.txt', 'r') as f:
    list1 = f.readlines()
    for line in list1:
        str1 = re.split(r'[\t\n]', line)
        # print(str1[0], str1[1], str1[2])
        sum[int(int(str1[1])/y_period)][int(int(str1[0])/x_period)] += float(str1[2])
        count[int(int(str1[1])/y_period)][int(int(str1[0])/x_period)] += 1
    grid = sum/count
# print(grid)

# np.savetxt('C:\Users\kgao\Documents\HMI\PyCharm\Heatmap\\count.txt', count, delimiter=',')
# np.savetxt('C:\Users\kgao\Documents\HMI\PyCharm\Heatmap\\grid.txt', grid, delimiter=',')

plt.imshow(grid, cmap='jet', interpolation='nearest', origin='lower', vmin=6.3, vmax=6.9)
plt.colorbar()
plt.show()