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
        arr[1] = int(arr[1])
    except:
        continue
    array.append(arr)

array.sort(key=lambda i: i[1])
tmp = 0
res = ''
for i in range(0, size):
    if array[i][1] == tmp:
        res = res + ',' + array[i][3]
    else:
        if len(res) > 0:
            print(res)
        tmp = array[i][1]
        print(tmp)
        res = array[i][3]
if len(res) > 0:
    print(res)