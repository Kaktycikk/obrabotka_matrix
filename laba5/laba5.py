# 27.	F(1) = 1; F(2) = 2; F(n) = (-1)n*(F(n-1)- F(n-3) /(2n)!) при n > 2
import math
import timeit
def recursive_f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fn_minus_3 = recursive_f(n - 3) if n > 3 else 1
        return (-1) ** n * (recursive_f(n - 1) - fn_minus_3 / math.factorial(2 * n))

def iterative_f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        f_prev = 1  
        f_curr = 2  
        minus = -1
        factorial_back = math.factorial(2 * 2)  
        for i in range(3, n + 1):
            factorial_now = factorial_back * (2 * i) * (2 * i - 1)
            f_next = minus * (f_prev - (f_curr / factorial_now))
            f_prev = f_curr
            f_curr = f_next
            minus *= -1
            factorial_back = factorial_now
        return f_curr

p = 1
while p == 1:
    n = int(input("Введите n: "))

    result_iterative = iterative_f(n)
    time_iterative = timeit.timeit("iterative_f(n)", globals=globals(), number=1)
    print(f"F({n}) (итеративно): {result_iterative}, время: {time_iterative} сек.")

    try:
        result_recursive = recursive_f(n)
        time_recursive = timeit.timeit("recursive_f(n)", globals=globals(), number=1)
        print(f"F({n}) (рекурсивно): {result_recursive}, время: {time_recursive} сек.")
    except RecursionError:
        print(f"Ошибка рекурсии при n = {n} (переполнение стека)")

    print("=" * 100)
    p = int(input("0/1: "))











