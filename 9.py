p = 0
o = 0
a = []
b = []
n = int(input('введите количество чисел'))
if n > 100 or n < 0:
    print('введите количество чисел, меньшее 100')
for i in range(n):
    m = int(input('введите числа'))
    if m < 0:
        a.append(m)
    else:
        b.append(m)
print(a , b)
