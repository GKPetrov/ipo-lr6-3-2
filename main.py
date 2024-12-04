import random
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
n = random.randint(4 , 8)
m = random.randint(4 , 8)
matrix = []
for i in range(n):
    matrix.append([0] * m)
for i in range(n): 
    for j in range(m):
        matrix[i][j] = numbers[random.randint(0 , 7)]
for i in range(len(matrix)):        
    for j in range(len(matrix[i])): 
        print(f"{matrix[i][j]:4}" , end = ' ')
    print() 
    sum = 0                   
for i in range(n): 
    for j in range(m):
        if matrix[i][j] % 3 == 0:
            sum += matrix[i][j] 
print(sum)
