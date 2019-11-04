def count_sort(a):
    k = max(a) + 1
    res = [0] * k
    for i in a:
        res[i] += 1
    for i in range(k):
        if res[i] > 0:
            print((str(i) + ' ') * res[i], end = '')
