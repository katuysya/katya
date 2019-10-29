def merge(L, R):
    result = []
    a = 0
    b = 0
    while a < len(L) and b < len(R):
        if L[a] <= R[b]:
            result.append(L[a])
            a += 1
        else:
            result.append(R[b])
            b += 1
    result += L[a:] + R[b:]
    return result
    
def merge_sort(x):
    N = len(x)
    if N <=  1:
        return x
    else:
        l_x = x[:N//2]
        r_x = x[N//2:]
    return merge(merge_sort(l_x), merge_sort(r_x))
a = [57, 22, 44, 10, 1, 213, 0, 76]
n = merge_sort(a)
print(n)
