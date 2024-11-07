# 27.	F(1) = 1; F(2) = 2; F(n) = (-1)n*(F(n-1)- F(n-3) /(2n)!) при n > 2
import math
import timeit
from functools import lru_cache
# Рекуррентная функция F(n) с использованием рекурсии
@lru_cache(maxsize=None)
def recursive_F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return (-1) ** 3 * (2 - 1 / math.factorial(6))  # Специальный случай для n=3
    else:
        return (-1) ** n * (recursive_F(n - 1) - recursive_F(n - 3) / math.factorial(2 * n))

# Рекуррентная функция F(n) с использованием итерации
def iterative_F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        f_values = [1, 2, (-1) ** 3 * (2 - 1 / math.factorial(6))]  # Начальные значения
        for i in range(4, n + 1):
            f_i = (-1) ** i * (f_values[-1] - f_values[-3] / math.factorial(2 * i))
            f_values.append(f_i)
        return f_values[-1]

# Функция для измерения времени выполнения
def measure_time(func, n):
    time_taken = timeit.timeit(lambda: func(n), number=100) / 100
    result = func(n)
    return result, time_taken

n = 10
# Рекурсивный подход
try:
    result_recursive, time_recursive = measure_time(recursive_F, n)
    print(f"Рекурсивный подход: F({n}) = {result_recursive}, время выполнения: {time_recursive:.8f} секунд")
except RecursionError:
    print(f"Ошибка: превышена максимальная глубина рекурсии для n={n}")

# Итерационный подход
result_iterative, time_iterative = measure_time(iterative_F, n)
print(f"Итерационный подход: F({n}) = {result_iterative}, время выполнения: {time_iterative:.8f} секунд")

# Сравнительная таблица
print("\nСравнительная таблица времени выполнения:")
print(f"{'Метод':<20}{'Результат':<20}{'Время выполнения (сек)'}")
if 'result_recursive' in locals():
    print(f"{'Рекурсивный':<20}{result_recursive:<20}{time_recursive:.8f}")
print(f"{'Итерационный':<20}{result_iterative:<20}{time_iterative:.8f}")