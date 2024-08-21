def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for g in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input("Укажите количество строк матрицы:"))
m = int(input("Укажите количество столбцов матрицы:"))
value = input("Укажите значения матрицы:")
matrix = get_matrix(n, m, value)

if n <= 0:
    print("Матрица пуста, указано неверное количество строк:", n)
elif m <=0:
    print("Матрица пуста, указано неверное количество столбцов:", m)
else:
    print("Матрица:")
    for i in matrix:
        print(*i)