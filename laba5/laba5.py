# 27.	F(1) = 1; F(2) = 2; F(n) = (-1)n*(F(n-1)- F(n-3) /(2n)!) при n > 2
import time
from functools import lru_cache

def precompute_factorials(max_n):
    """Вычисление факториалов (2n)! для n от 1 до max_n."""
    fact, factorials = 1, [1]
    for n in range(2, max_n + 1):
        fact *= (2 * n - 1) * (2 * n)
        factorials.append(fact)
    return factorials

@lru_cache(None)
def calculate_F_recursive(n, factorials):
    """Рекурсивное вычисление F(n) с использованием факториалов."""
    if n <= 0: return 0
    return 1 if n == 1 else 2 if n == 2 else (-1) ** n * (
        calculate_F_recursive(n - 1, factorials) - 
        calculate_F_recursive(n - 3, factorials) / factorials[n - 1])

def calculate_F_iterative(max_n, factorials):
    """Итерационное вычисление F(n)."""
    f1, f2, f3 = 1, 2, 0
    for n in range(3, max_n + 1):
        f1, f2, f3 = f2, f3, (-1) ** n * (f3 - f1 / factorials[n - 1])
    return f3 if max_n > 2 else (1 if max_n == 1 else 2)

def compare_methods(max_n, repeat=100):
    """Сравнение методов."""
    factorials = precompute_factorials(max_n)
    for n in range(1, max_n + 1):
        r_time = time.time()
        r_result = [calculate_F_recursive(n, tuple(factorials)) for _ in range(repeat)][0]
        i_time = time.time()
        i_result = [calculate_F_iterative(n, factorials) for _ in range(repeat)][0]

        print(f"{n:<5} {recur_time:<25.10f} {iter_time:<25.10f} {result_recur:<25.10f} {result_iter:<25.10f}")

compare_methods(20)



