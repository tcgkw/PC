import re
import os

hs_id = ['Test ID="0"', 'Test ID="1"', 'Test ID="2"', 'Test ID="3"', 'Test ID="4"', 'Test ID="5"', 'Test ID="6"', 'Test ID="7"']
l = 0
j = 0
list2 =[]
files = os.listdir('C:\\Users\\kgao\\Documents\\HMI\\Data\\Demo May 2018\\Micron\\L21\\For Marc\\L21_for_marc_07092018-1_201')
start = 0
end = 0


for file in files:
    if file.endswith('.bmp'):
        list2.append(file.split('-'))

list2.sort(key=lambda list2: (int(list2[3]), int(list2[4])))


with open('C:\Users\kgao\Documents\HMI\Data\Demo May 2018\Micron\L21\For Marc\L21_for_marc_07092018-1_201\\test.txt', 'r') as f:
    list1 = f.readlines()
    for i in hs_id:
        for line in list1[l:]:
            if i in line:
                start = j
                j += 1
                # print(i + str(start))
            if '</MeasureResult>' in line:
                end = j
                j += 1
                l = j
                # print(str(end) + 'end')
                break
            j += 1
        dd = 0
        for k in list1[(start + 4):(end-1)]:
            xx = int(134 * hs_id.index(i) + dd)
            k1 = re.sub('ImageID="\d+"', 'ImageID="1"', k)
            k2 = re.sub('ImageFile=".*.tif"', ('ImageFile="' + list2[xx][0] + '-' + list2[xx][1] + '-' + list2[xx][2] + '-'+ list2[xx][3] + '-' + list2[xx][4] + '-' + list2[xx][5] + '"'), k1)
            k3 = re.sub('ImageSize=".*" ImageFile=', 'ImageSize="8192 8192" ImageFile=', k2)
            list1[list1.index(k)] = k3
            dd += 1

with open('C:\Users\kgao\Documents\HMI\PyCharm\Temp\\result.txt', 'w') as wf:
    for line in list1:
        wf.write(line)
