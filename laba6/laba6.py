# У юноши P пиджаков, B брюк, R рубашек, G галстуков. Составьте все возможные костюмы из этих предметов.
import timeit
from itertools import product

# Часть 1 - Алгоритмическое решение
def algoritm(P, B, R, G):
    costumes = []
    for p in P:
        for b in B:
            for r in R:
                for g in G:
                    costumes.append((p, b, r, g))
    return costumes

# Часть 1 - Решение с помощью функций Python
def functionaly(P, B, R, G):
    return list(product(P, B, R, G))

# Часть 2 - Оптимизация: минимизация стоимости костюма
def find_min_cost_costume_functionaly(P, B, R, G, price_dict):
    min_cost = float('inf')
    best_costume = None
    costumes = product(P, B, R, G)
    for costume in costumes:
        total_cost = sum(price_dict[item] for item in costume)
        if total_cost < min_cost:
            min_cost = total_cost
            best_costume = costume
    return best_costume, min_cost

def find_min_cost_costume_algoritm(P, B, R, G, price_dict):
    min_cost = float('inf')
    best_costume = None
    costumes = []
    for p in P:
        for b in B:
            for r in R:
                for g in G:
                    costume = (p, b, r, g)
                    total_cost = sum(price_dict[item] for item in costume)
                    if total_cost < min_cost:
                        min_cost = total_cost
                        best_costume = costume
    return best_costume, min_cost

# Запрос данных у пользователя
def input_items(item_name):
    # Получаем количество предметов
    count = int(input(f"Введите количество {item_name}: "))
    # Создаем список с названиями предметов
    items = []
    for i in range(count):
        item_name_with_number = f"{item_name[0].lower()}{i+1}"  # p1, b1, r1, g1 и т.д.
        items.append(item_name_with_number)
    return items

# Запрос цен у пользователя
def input_prices(items):
    price_dict = {}
    for item in items:
        price = float(input(f"Введите цену для {item}: "))
        price_dict[item] = price
    return price_dict

# Чтение данных от пользователя
P = input_items("пиджаков")
B = input_items("брюк")
R = input_items("рубашек")
G = input_items("галстуков")
# Запрос цен для каждого предмета
price_dict = {}
price_dict.update(input_prices(P))
price_dict.update(input_prices(B))
price_dict.update(input_prices(R))
price_dict.update(input_prices(G))

# Часть 1 - замеры времени для алгоритмических и функциональных решений
start_time = timeit.default_timer()
result_algoritm = algoritm(P, B, R, G)
time_algoritm = timeit.default_timer() - start_time
start_time = timeit.default_timer()
result_functionaly = functionaly(P, B, R, G)
time_functionaly = timeit.default_timer() - start_time

# Вывод результатов Часть 1
print(f"Часть 1:")
print(f"Результат (алгоритмически): {result_algoritm}")
print(f"Время (алгоритмически): {time_algoritm:.6f} секунд.")
print(f"Результат (с помощью функции): {result_functionaly}")
print(f"Время (с помощью функции): {time_functionaly:.6f} секунд.")
print("=" * 50)

# Часть 2 -  поиск минимальной стоимости костюма
start_time = timeit.default_timer()
min_cost_costume_functionaly, min_cost_functionaly = find_min_cost_costume_functionaly(P, B, R, G, price_dict)
time_find_min_cost_functionaly = timeit.default_timer() - start_time
start_time = timeit.default_timer()
min_cost_costume_algoritm, min_cost_algoritm = find_min_cost_costume_algoritm(P, B, R, G, price_dict)
time_find_min_cost_algoritm = timeit.default_timer() - start_time

# Вывод результатов Часть 2
print(f"Часть 2:")
print(f"Минимальная стоимость костюма (с помощью функции): {min_cost_costume_functionaly}, стоимость: {min_cost_functionaly}")
print(f"Время (с помощью функции): {time_find_min_cost_functionaly:.6f} секунд.")
print(f"Минимальная стоимость костюма (алгоритмически): {min_cost_costume_algoritm}, стоимость: {min_cost_algoritm}")
print(f"Время (алгоритмически): {time_find_min_cost_algoritm:.6f} секунд.")




