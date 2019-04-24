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

print('here!')

with open(d2d_path_new, 'r') as dr:
    string = dr.readlines()[1:]

print(len(string))
