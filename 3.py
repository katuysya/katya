import math
result = 0
n = int(input('введите n'))
for i in range(n):
    a = int(input('введите а'))
    z = int(input('введите z'))
    beta = int(input('введите beta'))
    b = int(input('введите b'))
    x = z**3 - b + (a**2)/math.tan(beta)
    result += 1
print(result)
