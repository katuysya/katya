x1 = int(input('введите координату x1 точки'))
y1 = int(input('введите координату y1 точки'))

x2 = int(input('введите координату x2 точки'))
y2 = int(input('введите координату y2 точки'))

if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
    print('1')
elif x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0:
    print('2')
elif x1 > 0  and x2 > 0 and y1 < 0 and y2 < 0:
    print('3')
elif x1 and x2 < 0 and y1 < 0 and y2 < 0:
    print('4')
else:
    print('no')
