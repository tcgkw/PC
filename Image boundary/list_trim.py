import os
import re
import edge_detection

path = 'E:\Python\Image boundary'


list_bmp = []
files = os.listdir(path)
j = 0
for file in files:
    if os.path.splitext(files[j])[1] == '.bmp':  # 判断文件是否为bmp格式，如果是则存入list_bmp 备用
        list_bmp.append(os.path.splitext(file)[0])
    j += 1
print(list_bmp)
list1 = []
file = 'image-201-1-0-0-0.txt'
with open(path + '\\' + file, 'r') as f:
    lines = f.readlines()
    for line in lines[2:]:
        str_temp = re.split(r'[\s(),]', line)
        list1.append([str_temp[1], str_temp[3], str_temp[5]])

imported_list = list1

print(len(imported_list))

def trim_list(file, imported_list, list_bmp, b):    # b is buffer range to further reduce measure area
    output_list = imported_list
    if os.path.splitext(file)[0] in list_bmp:
        result = edge_detection.detect_edge(os.path.splitext(file)[0]+'.bmp')
        print(result)
        if result['x_dir'] == 'left edge' and result['y_dir'] == 'top edge':
            start_left = result['edge_px_x']
            end_top = result['edge_px_y']
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'center' and result['y_dir'] == 'top edge':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = result['edge_px_y']
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'right edge' and result['y_dir'] == 'top edge':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = result['edge_px_y']
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = result['edge_px_x']
        elif result['x_dir'] == 'left edge' and result['y_dir'] == 'center':
            start_left = result['edge_px_x']
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'center' and result['y_dir'] == 'center':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'right edge' and result['y_dir'] == 'center':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = min(int(line[1]) for line in imported_list)
            end_right = result['edge_px_x']
        elif result['x_dir'] == 'left edge' and result['y_dir'] == 'bottom edge':
            start_left = result['edge_px_x']
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = result['edge_px_y']
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'center' and result['y_dir'] == 'bottom edge':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = result['edge_px_y']
            end_right = max(int(line[0]) for line in imported_list)
        elif result['x_dir'] == 'right edge' and result['y_dir'] == 'bottom edge':
            start_left = min(int(line[0]) for line in imported_list)
            end_top = max(int(line[1]) for line in imported_list)
            start_bottom = result['edge_px_y']
            end_right = result['edge_px_x']
        else:
            print('Edge Detection Error!')

        print(start_left, start_bottom, end_right, end_top)

        for line in output_list:
                if int(line[0]) < int(start_left+b) or int(line[0]) > (end_right - b) or int(line[1]) < start_bottom+b or int(line[1]) > end_top-b:
                    output_list.remove(line)            ############# You are not permitted to remove elements from the list while iterating over it using a for loop
    return output_list

b = 200

output_list = trim_list(file,imported_list,list_bmp, b)
with open('E:\Python\PitchWalking_GUI\\tamp.txt', 'w') as w:
    for line in output_list:
        w.writelines(line)
        w.writelines('\n')
print(output_list[0][0])
print(len(output_list))