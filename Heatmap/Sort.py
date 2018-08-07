# import os
import re

with open('C:\Users\kgao\Documents\HMI\PyCharm\Heatmap\\test.txt', 'r') as f:
    list1 = f.readlines()
    list2 = []
    for line in list1:
        str1 = re.split(r'[\t\n]', line)
        list2.append([str1[0], str1[1], str1[2]])
    list2.sort(key=lambda list2 : (int(list2[1]),int(list2[0])))
with open('C:\Users\kgao\Documents\HMI\PyCharm\Heatmap\\temp.txt', 'w') as wf:
    for line in list2:
        wf.write(str(line[0]+'\t'+line[1]+'\t'+line[2]+'\n'))
