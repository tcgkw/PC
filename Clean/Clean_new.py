#-*- coding: utf-8 -*-


import numpy as np
import re
import os
import time
from collections import defaultdict

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

d2d_data_s = defaultdict(lambda: defaultdict(list))
d2db_data_s = defaultdict(lambda: defaultdict(list))

start_d2d_loading_time = time.time()

with open(d2d_path_new, 'r') as dr:
    temp = dr.readlines()
    for line in temp[1:]:
        print(temp.index(line))
        #check if image id exsits in dict, if in, add it to this key, if not, add key and
        d2d_image_id = line.split('\n')[0].split(',')[d2d_image_id_i]
        d2d_die_x = line.split('\n')[0].split(',')[d2d_die_x_i]
        d2d_die_y = line.split('\n')[0].split(',')[d2d_die_y_i]
        # if d2d_data_s.has_key(d2d_image_id):
        #     if d2d_data_s[d2d_image_id].has_key(d2d_die_x):
        d2d_data_s[d2d_image_id][d2d_die_x].append(d2d_die_y)
        #     else:
        #         d2d_data_s[d2d_image_id][d2d_die_x] = [d2d_die_y]
        # else:
        #     d2d_data_s[d2d_image_id] = {d2d_die_x: [d2d_die_y]}

        # print(type(d2d_data_s))
print(d2d_data_s)

print('Total D2D loading time is :', time.time() - start_d2d_loading_time)

start_d2db_loading_time = time.time()
with open(d2db_path_new, 'r') as drb:
    next(drb)
    i = 1
    for line in drb:
        print(i)
        #check if image id exsits in dict, if in, add it to this key, if not, add key and
        d2db_image_id = line.split('\n')[0].split(',')[d2db_image_id_i]
        d2db_die_x = line.split('\n')[0].split(',')[d2db_die_x_i]
        d2db_die_y = line.split('\n')[0].split(',')[d2db_die_y_i]
        # if d2d_data_s.has_key(d2d_image_id):
        #     if d2d_data_s[d2d_image_id].has_key(d2d_die_x):
        d2db_data_s[d2db_image_id][d2db_die_x].append(d2db_die_y)
        #     else:
        #         d2d_data_s[d2d_image_id][d2d_die_x] = [d2d_die_y]
        # else:
        #     d2d_data_s[d2d_image_id] = {d2d_die_x: [d2d_die_y]}

        # print(type(d2d_data_s))
        i += 1

print('Total D2DB loading time is :', time.time() - start_d2db_loading_time)

start_searching_time = time.time()
i = 0
print('here')
for image_id, die in d2db_data_s.items():
    if d2d_data_s.has_key(image_id):
        for x in d2d_data_s[image_id].keys():
            x_l = float(x) - r
            x_r = float(x) + r
            for die_x, die_y_list in d2db_data_s[image_id].items():
                if x_l < float(die_x) < x_r:
                    for d2d_y in d2d_data_s[image_id][x]:
                        y_u = float(d2d_y) + r
                        y_l = float(d2d_y) - r
                        for d2db_y in die_y_list:
                            if y_l < float(d2db_y) < y_u:
                                die_y_list.remove(d2db_y)
                    d2db_data_s[image_id][die_x] = die_y_list
                else:
                    continue
    else:
        continue


print('Total search time is :', time.time() - start_searching_time)

d2db_path_new2 = os.path.splitext(d2db_path)
d2db_path_new2 = d2db_path_new2[0] + 'trimmed' + d2db_path_new2[1]
with open(d2db_path_new2, 'w+') as fw:
    for image_id, die in d2db_data_s.items():
        for die_x, die_y_list in d2db_data_s[image_id].items():
            for line in die_y_list:
                str1 = image_id + ',' + die_x + ',' + line
                fw.writelines(str1)
