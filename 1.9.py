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
            arr[i] = int(arr[i])
    except:
        continue
    array.append(arr)

array.sort(key=lambda i: len(i))

res = []
for arr in array[0]:
    flag = 1
    for i in range(1, size):
        if arr not in array[i]:
            flag = 0
    if flag == 1:
        res.append(arr)
res.sort()
pr =''
for i in range(0, len(res)):
    if len(pr) > 0:
        pr += ','
    pr += str(res[i])
print(pr)
