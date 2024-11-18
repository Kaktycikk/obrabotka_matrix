# У юноши P пиджаков, B брюк, R рубашек, G галстуков. Составьте все возможные костюмы из этих предметов.
import time
from itertools import product

def generate_costumes_algorithmic(jackets, trousers, shirts, ties, restrictions=None):
    """Алгоритмический способ генерации всех возможных костюмов с учётом ограничений."""
    costumes = []
    for jacket in jackets:
        for trouser in trousers:
            if restrictions and not restrictions.get((jacket, trouser), True):
                continue  # Пропускаем несочетаемые пиджак и брюки
            for shirt in shirts:
                for tie in ties:
                    if restrictions and not restrictions.get((shirt, tie), True):
                        continue  # Пропускаем несочетаемые рубашку и галстук
                    costumes.append((jacket, trouser, shirt, tie))
    return costumes

def generate_costumes_with_itertools(jackets, trousers, shirts, ties, restrictions=None):
    """Генерация костюмов с помощью itertools.product с учётом ограничений."""
    all_combinations = product(jackets, trousers, shirts, ties)
    if restrictions:
        # Фильтруем комбинации по ограничениям
        return [
            combo for combo in all_combinations
            if restrictions.get((combo[0], combo[1]), True) and restrictions.get((combo[2], combo[3]), True)
        ]
    return list(all_combinations)

def add_style_scores(costumes, style_scores):
    """Добавляет баллы стиля для каждого костюма."""
    return [
        (costume, sum(style_scores.get(item, 0) for item in costume))
        for costume in costumes
    ]

def measure_execution_time(func, *args):
    """Замер времени выполнения функции."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time

def main():
    # Пример данных
    jackets = ['J1', 'J2', 'J3']  # Пиджаки
    trousers = ['T1', 'T2']       # Брюки
    shirts = ['S1', 'S2', 'S3']   # Рубашки
    ties = ['G1', 'G2']           # Галстуки
    # Ограничения
    restrictions = {
        ('J3', 'T1'): False,  # J3 нельзя носить с T1
        ('S2', 'G1'): False   # S2 нельзя носить с G1
    }
    # Баллы стиля
    style_scores = {
        'J1': 5, 'J2': 7, 'J3': 10,
        'T1': 3, 'T2': 6,
        'S1': 2, 'S2': 4, 'S3': 5,
        'G1': 1, 'G2': 3
    }
    # Генерация костюмов алгоритмическим способом
    algo_result, algo_time = measure_execution_time(
        generate_costumes_algorithmic, jackets, trousers, shirts, ties, restrictions
    )
    # Генерация костюмов с помощью itertools
    itertools_result, itertools_time = measure_execution_time(
        generate_costumes_with_itertools, jackets, trousers, shirts, ties, restrictions
    )

    # Проверка совпадения результатов
    assert set(algo_result) == set(itertools_result), "Результаты генерации не совпадают!"
    # Добавляем баллы стиля
    algo_result_with_scores = add_style_scores(algo_result, style_scores)
    # Сортируем по стилю
    algo_result_with_scores.sort(key=lambda x: x[1], reverse=True)

    # Вывод результатов
    print(f"Алгоритмический способ: {len(algo_result)} костюмов, время {algo_time:.6f} секунд")
    print(f"С использованием itertools: {len(itertools_result)} костюмов, время {itertools_time:.6f} секунд")
    print("\nВсе возможные костюмы (с баллами стиля):")
    for costume, score in algo_result_with_scores: print(f"Костюм: {costume}, Баллы стиля: {score}")

if __name__ == "__main__":
    main()



