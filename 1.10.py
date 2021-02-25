import datetime
size = input()
try:
    size = int(size)
except:
    size = 0
array = []
for i in range(0, size):
    inp = input()
    try:
        arr = inp.split(',')
        for i in range(0, len(arr)):
            arr[i] = datetime.datetime.strptime(arr[i], '%Y-%m-%dT%H:%M')
    except:
        continue
    array.append(arr)

for i in range(0, size):
    if array[i][2] > array[i][0]:
        t1 = array[i][2] - array[i][0]
    else:
        t1 = array[i][0] - array[i][2]
    if array[i][3] > array[i][1]:
        t2 = array[i][3] - array[i][1]
    else:
        t2 = array[i][1] - array[i][3]
    if t1.seconds < 1800 and t2.seconds < 1800:
        print('Yes')
    else:
        print('No')


