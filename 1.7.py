src = input()
try:
    srclist = src.split(',')
except:
    srclist = []
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
        #arr[1] = int(arr[1])
    except:
        continue
    array.append(arr)

for i in range(0, size):
    if array[i][1] in srclist:
        print(array[i][0] + ',' + array[i][1] + ',' + array[i][2] + ',' + array[i][3])
