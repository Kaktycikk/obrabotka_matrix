# 27.	F(1) = 1; F(2) = 2; F(n) = (-1)n*(F(n-1)- F(n-3) /(2n)!) при n > 2
import math
import time
from functools import lru_cache

# Предварительное вычисление факториалов
def precompute_factorials(max_n):
    """Вычисление факториалов для всех значений (2n)! от 1 до max_n."""
    factorials = [1]  # Начинаем с (2*1)!
    fact = 1
    for n in range(2, max_n + 1):
        fact *= (2 * n - 1) * (2 * n)
        factorials.append(fact)
    return factorials

# рекурсивная функция с мемоизацией
@lru_cache(maxsize=None)
def calculate_F_recursive(n, factorials):
    """Рекурсивный метод вычисления F(n) с использованием заранее подготовленных факториалов."""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n <= 0:
        return 0  # Базовый случай для отрицательных индексов
    else:
        return (-1) ** n * (
            calculate_F_recursive(n - 1, factorials) -
            calculate_F_recursive(n - 3, factorials) / factorials[n - 1]
        )

# Итеративный метод
def calculate_F_iterative(max_n, factorials):
    """Итерационный метод вычисления F(n) с использованием заранее подготовленных факториалов."""
    if max_n == 1:
        return 1
    elif max_n == 2:
        return 2

    f1, f2, f3 = 1, 2, 0  # F(n-3), F(n-2), F(n-1)
    for n in range(3, max_n + 1):
        fn = (-1) ** n * (f3 - f1 / factorials[n - 1])
        # Сдвигаем значения для следующей итерации
        f1, f2, f3 = f2, f3, fn

    return fn

def compare_methods(max_n, repeat=100):
    """Сравнение времени выполнения итерационного и рекурсивного методов."""
    # Предварительно вычисляем факториалы
    factorials = precompute_factorials(max_n)
    print(f"{'n':<5} {'Время рекурсии (сек)':<25} {'Время итерации (сек)':<25} {'Результат рекурсии':<25} {'Результат итерации':<25}")

    for n in range(1, max_n + 1):
        # Рекурсивный метод
        start_time = time.perf_counter()
        for _ in range(repeat):
            result_recur = calculate_F_recursive(n, tuple(factorials))
        recur_time = (time.perf_counter() - start_time) / repeat

        # Итерационный метод
        start_time = time.perf_counter()
        for _ in range(repeat):
            result_iter = calculate_F_iterative(n, factorials)
        iter_time = (time.perf_counter() - start_time) / repeat

        print(f"{n:<5} {recur_time:<25.10f} {iter_time:<25.10f} {result_recur:<25.10f} {result_iter:<25.10f}")

compare_methods(20)



