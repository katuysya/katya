import collections
def simple(x):
    counter = 0
    for i in range(1, x+1):
        if x % i == 0:
            counter += 1
    if counter == 2:
         return True
    else:
        return False

arr = input().split()
arr1 = []
arr2 = []
summ = 0
for i in arr:
    for j in i:
        summ += int(j)
    if simple(summ):
        arr1.append(summ)
    summ = 0

c = collections.Counter(arr1).most_common(1)
c1 = dict(c)
print(c1.values())
