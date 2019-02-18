n = int(input('введите количество троек n'))
mini = 0
maxi = 0
s = 0
m = 0
k = 0
l = 0
f = 0
for i in range(n):
    a = int(input('введите число'))
    b = int(input('введите число'))
    c = int(input('введите число'))
    mini = min(a, b, c)
    maxi = max(a, b, c)
    if mini == a and maxi == b or mini == b and maxi == a:
        m = c
    elif mini == c and maxi == a or mini == a and maxi == c:
        m = b
    elif mini == b and maxi == c or mini == c and maxi == b:
        m = a
    l = l + mini
    k = k + m
    f = f + maxi
    if l % 5 != 0:
        s = l
    elif l % 5 == 0 and k % 5 != 0:
        s = k
    elif l % 5 == 0 and k % 5 == 0 and f % 5 != 0:
        s = f
    else:
        s = s
print(s)
