import os



list1 = []
with open('X:\\temp.txt', 'r') as f:
    bmp = f.readlines()
    for line in bmp:
        list1.append(line.split('-'))
    print(list1[0])



