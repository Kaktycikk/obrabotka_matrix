import random

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    N = int(lines[0].strip())
    matrix = [list(map(int, line.strip().split())) for line in lines[1:]]
    return N, matrix

def generate_random_matrix(N, low=-10, high=10):
    return [[random.randint(low, high) for _ in range(N)] for _ in range(N)]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def get_triangles(matrix):
    N = len(matrix)
    triangle_1 = []
    triangle_2 = []
    triangle_4 = []

    for i in range(N):
        for j in range(N):
            if i > j and i + j < N - 1:
                triangle_1.append(matrix[i][j])

    for j in range(N-1, -1, -1):
        for i in range(N):
            if i < j and i + j < N - 1:
                triangle_2.append(matrix[i][j])

    for j in range(N-1, -1, -1):
        for i in range(N-1, -1, -1):
            if i > j and i + j > N - 1:
                triangle_4.append(matrix[i][j])

    return triangle_1, triangle_2, triangle_4

def get_zero_count(triangle):
    return triangle.count(0)

def get_product(triangle):
    product = 1
    for num in triangle:
        if num != 0:
            product *= num
    return product

def transpose(matrix):
    N = len(matrix)
    return [[matrix[j][i] for j in range(N)] for i in range(N)]

def add_matrices(A, B):
    N = len(A)
    return [[A[i][j] + B[i][j] for j in range(N)] for i in range(N)]

def subtract_matrices(A, B):
    N = len(A)
    return [[A[i][j] - B[i][j] for j in range(N)] for i in range(N)]

def multiply_matrices(A, B):
    N = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]

def sym_replace_area_1_and_4(F, triangle_1, triangle_4):
    N = len(F)
    idx_1 = 0
    idx_4 = 0

    for i in range(N):
        for j in range(N):
            if i > j and i + j < N - 1:
                F[i][j] = triangle_4[idx_4]
                idx_4 += 1

    for i in range(N):
        for j in range(N):
            if i > j and i + j > N - 1:
                F[i][j] = triangle_1[idx_1]
                idx_1 += 1

    return F

def asym_replace_area_1_and_2(F, triangle_1, triangle_2):
    N = len(F)

    idx_1 = 0
    idx_2 = 0

    for j in range(N - 1, 0, -1):
        for i in range(j):
            if i < j and i + j < N - 1:
                F[i][j] = triangle_1[idx_1]
                idx_1 += 1

    for i in range(1, N):
        for j in range(i):
            if i > j and i + j < N - 1:
                F[i][j] = triangle_2[idx_2]
                idx_2 += 1

    return F
# Основная логика программы
choice = input("Выберите метод заполнения матрицы (1 - случайное, 2 - из файла): ")

if choice == '1':
    N = int(input("Введите размер матрицы N (от 3 до 10): "))
    A = generate_random_matrix(N)
    print("Сгенерированная матрица A:")
    print_matrix(A)
elif choice == '2':
    file_path = "matr.txt"
    N, A = read_matrix_from_file(file_path)
    print("Матрица A из файла: ")
    print_matrix(A)
else:
    print("Неверный выбор")

F = [row[:] for row in A]

triangle_1, triangle_2, triangle_4 = get_triangles(A)

print("\nТреугольник 1 (левый треугольник):", triangle_1)
print("Треугольник 2 (верхний треугольник):", triangle_2)
print("Треугольник 4 (нижний треугольник):", triangle_4)

zero_count_2 = get_zero_count(triangle_2)
product_4 = get_product(triangle_4)

if zero_count_2 > product_4:
    print("Выполняется симметричная замена областей 1 и 4")
    F = sym_replace_area_1_and_4(F, triangle_1, triangle_4)
else:
    print("Выполняется несимметричная замена областей 1 и 2")
    F = asym_replace_area_1_and_2(F, triangle_1, triangle_2)

print("\nМатрица F после замены:")
print_matrix(F)

K = int(input("Введите K: "))
AT = transpose(A)
FT = transpose(F)

K_AT = [[K * AT[i][j] for j in range(N)] for i in range(N)]

F_plus_A = add_matrices(F, A)

K_AT_F_plus_A = multiply_matrices(K_AT, F_plus_A)

K_FT = [[K * FT[i][j] for j in range(N)] for i in range(N)]

result = subtract_matrices(K_AT_F_plus_A, K_FT)

print("\nРезультат выражения ((K * A^T) * (F + A) - K * F^T):")
print_matrix(result)









