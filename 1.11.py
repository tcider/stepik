dct = {'Scheduled': 0, 'On Time': 0, 'Delayed': 0, 'Departed': 0, 'Arrived': 0, 'Cancelled': 0}
size = input()
try:
    size = int(size)
except:
    size = 0

for i in range(0, size):
    inp = input()
    try:
        arr = inp.split(',')
        dct[arr[1]] += 1
    except:
        continue

print(dct['Scheduled'])
print(dct['On Time'])
print(dct['Delayed'])
print(dct['Departed'])
print(dct['Arrived'])
print(dct['Cancelled'])

