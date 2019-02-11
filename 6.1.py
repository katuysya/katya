import random 
x = int(input('введите координату точки x'))
y = int(input('введите координату точки y'))
s1 = random.randint(1, 4)
s2 = random.randint(1, 2)
s3 = random.randint(3, 4)
s4 = random.randrange(1, 4)
s5 = random.randrange(2, 3)
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y == 0:
    print(s1)
elif x == 0 and y > 0:
    print(s2)
elif x == 0 and y < 0:
    print(s3)
elif x > 0 and y == 0:
    print(s4)
elif x < 0 and y == 0:
    print(s5)
