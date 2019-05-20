class matrix2x2(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
         return self.items.pop()
    def det(self):
        self.determ = x1*x4 - x2*x3

matrix = matrix2x2()
#тут я пытаюсь создать матрицу
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
#первая строка матрицы
part1 = []
part1.append(x1)
part1.append(x2)
#вторая строка матрицы
part2 = []
part2.append(x3)
part2.append(x4)
matrix.push(part1)
matrix.push(part2)
#находим детерминант
matrix.det()

print(matrix.determ)
