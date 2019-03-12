n = int(input('введите размерность матрицы')) 
m1 = [] 
for i in range(n): 
s = input() 
m1.append(s.split(' ')) 
m2 = [] 
for i in range(n): 
s = input('.') 
m2.append(s.split(' ')) 
k = [[''for i in range(n)] for i in range(n)] 
for i in range(n): 
for j in range(i, n): 
k[i][j] = int(m1[i][j])* int(m2[j][i]) 
print(k)
