import math
N = int(input())
counter = 0
arr = [0]*10
for i in range(N):
    k = int(input())
    k = k%10
    arr[k]+= 1
if arr[5]>=2:
    f = math.factorial(arr[5])
    l = math.factorial(2)
    c = math.factorial((arr[5]-2))
    counter = f//(c*l)
if arr[10]>=2:
    v = math.factorial(arr[10])
    r = math.factorial(2)
    p = math.factorial((arr[10]-2))
    counter1 = v//(r*p)    
print(arr[1]*arr[9] + arr[2]*arr[8] + arr[3]*arr[7] + arr[4]*arr[6] + counter + counter1)
