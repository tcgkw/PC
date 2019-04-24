#-*- coding: utf-8 -*-

import numpy as np
import re
import os
import time

r = 0.00005
d2d_path = 'E:\\Python\\Clean\\D2D2.csv'
d2db_path = 'E:\\Python\\Clean\\0329D2DB2_less.csv'
result = np.array([])
start_loading_time = time.time()

with open(d2d_path, 'r') as do:
    d2d_data = do.readlines()
    for line in d2d_data:
        # print(line)
        # m = re.findall(r'"\(\d(.).{1}\d\)"', line)
        m = re.findall(r'"\(\D{0,1}\d*\D{1,2}\d*\)"', line)
        if m != []:
            # print(m[0])
            x = m[0].split(',')
            # print(x)
            pattern = re.compile(r'"\(\D{0,1}\d*\D{1,2}\d*\)"')
            i = d2d_data.index(line)
            d2d_data[i] = pattern.sub(x[0] + '_' + x[1], line)
            # print(c)

d2d_path_new = os.path.splitext(d2d_path)
d2d_path_new = d2d_path_new[0] + '_temp' + d2d_path_new[1]
header = d2d_data[0].split('\n')[0].split(',')
# print(header)

d2d_image_id_i = header.index('Image ID')
d2d_die_x_i = header.index('Defect PosX for die')
d2d_die_y_i = header.index('Defect PosY for die')
# print(d2d_image_id_i, d2d_die_x_i, d2d_die_y_i)

with open(d2d_path_new, 'w+') as nw:
    nw.writelines(d2d_data)


with open(d2db_path, 'r') as dob:
    d2db_data = dob.readlines()
    for line in d2db_data:
        m = re.findall(r'"\(\D{0,1}\d*\D{1,2}\d*\)"', line)
        if m != []:
            x = m[0].split(',')
            pattern = re.compile(r'"\(\D{0,1}\d*\D{1,2}\d*\)"')
            i = d2db_data.index(line)
            d2db_data[i] = pattern.sub(x[0] + '_' + x[1], line)

d2db_path_new = os.path.splitext(d2db_path)
d2db_path_new = d2db_path_new[0] + '_temp' + d2db_path_new[1]
header_b = d2db_data[0].split('\n')[0].split(',')
# print(header_b)
d2db_image_id_i = header_b.index('Image ID')
d2db_die_x_i = header_b.index('Die Pos X')
d2db_die_y_i = header_b.index('Die Pos Y')
# print(d2db_image_id_i, d2db_die_x_i, d2db_die_y_i)

with open(d2db_path_new, 'w+') as nw:
    nw.writelines(d2db_data)
print('here1')
try:
    d2d_data_s = np.genfromtxt(d2d_path_new, usecols=(d2d_image_id_i, d2d_die_x_i, d2d_die_y_i), delimiter=',')
    d2db_data_s = np.genfromtxt(d2db_path_new, usecols=(d2db_image_id_i, d2db_die_x_i, d2db_die_y_i), delimiter=',')
    print('here2')
except Exception as aaaa:
    print(aaaa)

print('here3')

end_loading_time = time.time()
print('Loading time is', end_loading_time - start_loading_time)


def search(d2d_image_id, d2d_die_x, d2d_die_y):
    x_l = d2d_die_x - r
    x_r = d2d_die_x + r
    y_u = d2d_die_y + r
    y_l = d2d_die_y - r
    xx = np.where((d2db_data_s[:, 0] == d2d_image_id) & (x_l < d2db_data_s[:, 1]) & (d2db_data_s[:, 1] < x_r) & (
            y_l < d2db_data_s[:, 2]) & (d2db_data_s[:, 2] < y_u))
    return xx[0]


start_searching_time = time.time()

for i in range(d2d_data_s.shape[0]):
    s_time = time.time()
    print(i)
    d2d_image_id = d2d_data_s[i][0]
    d2d_die_x = d2d_data_s[i][1]
    d2d_die_y = d2d_data_s[i][2]
    t = search(d2d_image_id, d2d_die_x, d2d_die_y)
    print(t)
    result = np.append(result, t)
    print('Single search time is:', time.time() - s_time)

print(result)
print('Total search time is :', time.time() - start_searching_time)
