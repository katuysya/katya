x = int(input('введите координату точки x'))
y = int(input('введите координату точки y'))
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    print('введите  x и y, неравные нулю')
