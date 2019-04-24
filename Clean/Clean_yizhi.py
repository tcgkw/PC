
"""
Raw data type:
d2d_data = [[ImageID, x, y], [],]
d2db_data = [[ImageID, x, y]]
"""


START = [0, 0]
END = [10, 10]
Accuracy = 5

def preProcess(rawData, imageID):
    for i, ele in enumerate(rawData):
        imageId, x, y = rawData[i]
        val = encode(x, y, START, END, Accuracy)  # need to predefine start_point, end_point, n
        imageID[imageId].append(val)
    return


def encode(x, y, start_point, end_point, n):
    ans = [0]
    def helper(start_point, end_point, n, ans):
        if n == 0:
            return
        x_step = (end_point[0] - start_point[0]) / 3.0
        y_step = (end_point[1] - start_point[1]) / 3.0
        x_grid = min(int((x - start_point[0]) / x_step), 2)
        y_grid = min(int((y - start_point[1]) / y_step), 2)

        curr = y_grid * 3 + x_grid + 1
        next_start = [start_point[0] + x_step * x_grid, start_point[1] + y_step * y_grid]
        next_end = [next_start[0] + x_step, next_start[1] + y_step]
        ans[0] = ans[0] * 10 + curr
        return helper(next_start, next_end, n - 1, ans)
    helper(start_point, end_point, n, ans)
    return ans[0]


def search(val, table):
    if val < table[0] or val > table[-1]:
        return False
    l, r = 0, len(table)-1
    while (l<r):
        mid = l + (r-l)//2
        if table[mid] >= val:
            r = mid
        else:
            l = mid + 1
    if table[l] == val:
        return True
    return False




imageID_d2d = collections.defaultdict(lambda : [])

preProcess(d2d_data, imageID_d2d)

# sorting for d2d
for imageId in imageID_d2d:
    imageID_d2d[imageId].sort()

# ans is the index need to be deleted  in d2db
ans = []

for i, ele in enumerate(d2db_data):
    imageId, x, y = d2db_data
    if imageId not in imageID_d2d:
        continue
    val = encode(x, y, START, END, Accuracy)
    if search(val, imageID_d2d[imageId]):
        ans.append(i)

return ans



