import re

with open('Y:\Python\Heat map\\temp\\temp.txt', 'r') as f:
    list2 = f.readlines()
    str1 = re.split(r'[\t\n]', list2[0])
    print(str1)