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

dct = dict()
max = 0
for i in range(0, size):
    if array[i][1] in dct:
        dct[array[i][1]] += 1
    else:
        dct[array[i][1]] = 1
    if dct[array[i][1]] > max:
        max = dct[array[i][1]]

keys = []
dctlist = list(dct.items())
for d in dctlist:
    if d[1] == max:
        keys.append(d[0])

keys.sort()
res = ''
for k in keys:
    if len(res) > 0:
        res += ' '
    res += str(k)

print(res)
