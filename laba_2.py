"""Формируется матрица F следующим образом: скопировать в нее А и  если в Е сумма
чисел по периметру больше, чем количество нулей по периметру , то поменять местами
В и С симметрично, иначе В и Е поменять местами несимметрично. При этом матрица
А не меняется. После чего если определитель матрицы А больше суммы диагональных
элементов матрицы F, то вычисляется выражение: A*AT – K * F, иначе вычисляется
выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно."""

import numpy as np
import matplotlib.pyplot as plt
# функции
def generate_random_matrix(N):
    return np.random.randint(-10, 11, size=(N, N))

def print_matrix(matrix):
    print('\n'.join(' '.join(map(str, row)) for row in matrix))

def read_matrix_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    N = int(lines[0].strip())
    matrix = np.array([list(map(int, line.strip().split())) for line in lines[1:]])  # Преобразуем в NumPy массив
    return N, matrix

def get_matrix(matrix, N):
    half = N // 2
    if N % 2 == 0:
        matrix_B = matrix[:half, :half]
        matrix_C = matrix[:half, half:]
        matrix_D = matrix[half:, :half]
        matrix_E = matrix[half:, half:]
    else:
        matrix_B = matrix[:half, :half]
        matrix_C = matrix[:half, half + 1:]
        matrix_D = matrix[half + 1:, :half]
        matrix_E = matrix[half + 1:, half + 1:]

    return matrix_B, matrix_C, matrix_D, matrix_E

def sum_perimeter(matrix):
    return sum(matrix[0]) + sum(matrix[-1]) + sum(row[0] + row[-1] for row in matrix[1:-1])

def count_zeros_on_perimeter(matrix):
    return (sum(x == 0 for x in matrix[0]) + sum(x == 0 for x in matrix[-1]) +
            sum(row[0] == 0 for row in matrix[1:-1]) + sum(row[-1] == 0 for row in matrix[1:-1]))

def compare_and_replace(F, matrix_B, matrix_C, matrix_E):
    sum_E = sum_perimeter(matrix_E)
    zeros_E = count_zeros_on_perimeter(matrix_E)

    if sum_E > zeros_E:
        print("Симметричная замена B и C")
        F[:matrix_B.shape[0], :matrix_B.shape[1]] = matrix_C
        F[matrix_B.shape[0]:, :matrix_C.shape[1]] = matrix_B
    else:
        print("Несимметричная замена B и E")
        temp_B = matrix_B.copy()
        F[:matrix_B.shape[0], :matrix_B.shape[1]] = matrix_E
        F[:matrix_E.shape[0], matrix_B.shape[1]:] = temp_B

    return F

def plot_matrix(matrix, title):
    plt.figure()
    plt.imshow(matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title(title)
    plt.show()

def plot_histogram(matrix):
    plt.figure()
    plt.hist(matrix.flatten(), bins=20, alpha=0.7, color='blue')
    plt.title("Гистограмма значений матрицы F")
    plt.xlabel("Значения")
    plt.ylabel("Частота")
    plt.show()

def plot_heatmap(matrix):
    plt.figure()
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.title("Тепловая карта значений матрицы F")
    plt.colorbar()
    plt.show()

def calculate_expression(A, F, K):
    det_A = np.linalg.det(A)
    sum_diag_F = np.trace(F)

    if det_A > sum_diag_F:
        print("Выполняется выражение: A * AT - K * F")
        AT = np.transpose(A)
        result = np.dot(A, AT) - K * F
    else:
        print("Выполняется выражение: (A^-1 + G - F^-1) * K")
        # Вычисляем обратную матрицу A и F
        A_inv = np.linalg.inv(A)
        F_inv = np.linalg.inv(F)
        G = np.tril(A)
        result = (A_inv + G - F_inv) * K

    return result
# основная логика программы
K = int(input("Введите число K: "))

choice = input("Выберите метод заполнения матрицы (1 - случайное, 2 - из файла): ")
if choice == '1':
    N = int(input("Введите размер матрицы N (от 3 до 100): "))
    if N < 3 or N > 100:
        print("Введите число в указанном диапазоне")
    else:
        A = generate_random_matrix(N)
        print("Сгенерированная матрица A: ")
        print_matrix(A)
elif choice == '2':
    file_path = "matr.txt"
    N, A = read_matrix_from_file(file_path)
    print("Матрица A из файла: ")
    print_matrix(A)
else:
    print("Неверный выбор")

F = A.copy()
print("Матрица F:\n", end=""); print_matrix(F)
matrix_B, matrix_E, matrix_C, matrix_D = get_matrix(A, N)

for name, mat in zip(["B", "E", "C", "D"], [matrix_B, matrix_E, matrix_C, matrix_D]):
    print(f"Матрица {name}:")
    print_matrix(mat)
F = compare_and_replace(F, matrix_B, matrix_C, matrix_E)
print("Обновленная матрица F:\n", end=""); print_matrix(F)
plot_matrix(F, "Обновленная матрица F после замены")
result = calculate_expression(A, F, K)
print("Вывод выражения:\n", end=""); print_matrix(result)
plot_histogram(F)  # Второй график
plot_heatmap(result)