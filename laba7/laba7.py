from tkinter import *
from tkinter import messagebox
from itertools import product

# Функция для вычисления минимальной стоимости костюма
def calculate_min_cost_costume(P, B, R, G, price_dict):
    min_cost = float('inf')
    best_costume = None
    for costume in product(P, B, R, G):  # Все возможные комбинации
        total_cost = sum(price_dict[item] for item in costume)
        if total_cost < min_cost:
            min_cost = total_cost
            best_costume = costume
    return best_costume, min_cost

# Функция, которая вызывается при нажатии на кнопку "Вычислить"
def on_calculate_button_click(window, p_input, b_input, r_input, g_input, p_prices, b_prices, r_prices, g_prices):
    try:
        # Ввод товаров
        P = p_input.get("1.0", "end-1c").split()
        B = b_input.get("1.0", "end-1c").split()
        R = r_input.get("1.0", "end-1c").split()
        G = g_input.get("1.0", "end-1c").split()

        # Ввод цен
        p_prices_list = p_prices.get("1.0", "end-1c").split()
        b_prices_list = b_prices.get("1.0", "end-1c").split()
        r_prices_list = r_prices.get("1.0", "end-1c").split()
        g_prices_list = g_prices.get("1.0", "end-1c").split()

        # Проверка на соответствие количеству предметов
        if len(p_prices_list) != len(P) or len(b_prices_list) != len(B) or len(r_prices_list) != len(R) or len(g_prices_list) != len(G):
            messagebox.showwarning("Ошибка!", "Количество цен должно соответствовать количеству предметов!")
            return

        # Создаем соответствие между предметами и ценами
        price_dict = {item: int(price) for item, price in zip(P + B + R + G, p_prices_list + b_prices_list + r_prices_list + g_prices_list)}

        # Проверка на пустые данные
        if not P or not B or not R or not G or not price_dict:
            messagebox.showwarning("Ошибка!", "Заполните все поля данных!")
            return

        # Рассчитываем минимальный костюм
        best_costume, min_cost = calculate_min_cost_costume(P, B, R, G, price_dict)

        # Закрываем окно ввода перед открытием окна вывода
        window.destroy()

        # Выводим результат
        output_window(best_costume, min_cost, P, B, R, G)

    except ValueError:
        messagebox.showwarning("Ошибка!", "Пожалуйста, введите правильные данные!")

# Окно вывода с результатами
def output_window(best_costume, min_cost, P, B, R, G):
    output_window = Tk()
    output_window.title("Результаты расчёта")
    center_window(output_window, 800, 600)  # Увеличено до 800x600

    frame = Frame(output_window, bg="lightgray")
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    result_label = Label(frame, text="Минимальный костюм и его стоимость:", font=("Arial", 16))
    result_label.pack(pady=10)

    costume_label = Label(frame, text=f"Костюм: {best_costume}", font=("Arial", 14))
    costume_label.pack(pady=10)

    cost_label = Label(frame, text=f"Стоимость: {min_cost} руб.", font=("Arial", 14))
    cost_label.pack(pady=10)

    back_button = Button(frame, text="Назад", font=("Arial", 14), command=output_window.destroy)
    back_button.pack(pady=20)

    output_window.mainloop()

# Функция для центрирования окна на экране
def center_window(window, width, height):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Основное окно ввода данных
def enter_window():
    window = Tk()
    window.title("Окно ввода данных")
    center_window(window, 800, 800)  # Увеличено до 800x800
    window.resizable(width=False, height=False)

    frame = Frame(window, bg="lightgray")
    frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    instruction_label = Label(frame, text="Введите предметы одежды через пробел (например, P1 P2 P3)", font=("Arial", 14))
    instruction_label.pack(pady=10)

    p_label = Label(frame, text="Пиджаки (P1...):", font=("Arial", 12))
    p_label.pack()
    p_input = Text(frame, height=2, font=("Arial", 12))
    p_input.pack(pady=5)

    p_prices_label = Label(frame, text="Введите цены для пиджаков (например, 10 20 30):", font=("Arial", 12))
    p_prices_label.pack()
    p_prices = Text(frame, height=2, font=("Arial", 12))
    p_prices.pack(pady=5)

    b_label = Label(frame, text="Брюки (B1...):", font=("Arial", 12))
    b_label.pack()
    b_input = Text(frame, height=2, font=("Arial", 12))
    b_input.pack(pady=5)

    b_prices_label = Label(frame, text="Введите цены для брюк (например, 10 20 30):", font=("Arial", 12))
    b_prices_label.pack()
    b_prices = Text(frame, height=2, font=("Arial", 12))
    b_prices.pack(pady=5)

    r_label = Label(frame, text="Рубашки (R1...):", font=("Arial", 12))
    r_label.pack()
    r_input = Text(frame, height=2, font=("Arial", 12))
    r_input.pack(pady=5)

    r_prices_label = Label(frame, text="Введите цены для рубашек (например, 10 20 30):", font=("Arial", 12))
    r_prices_label.pack()
    r_prices = Text(frame, height=2, font=("Arial", 12))
    r_prices.pack(pady=5)

    g_label = Label(frame, text="Галстуки (G1...):", font=("Arial", 12))
    g_label.pack()
    g_input = Text(frame, height=2, font=("Arial", 12))
    g_input.pack(pady=5)

    g_prices_label = Label(frame, text="Введите цены для галстуков (например, 10 20 30):", font=("Arial", 12))
    g_prices_label.pack()
    g_prices = Text(frame, height=2, font=("Arial", 12))
    g_prices.pack(pady=5)

    calculate_button = Button(frame, text="Вычислить", font=("Arial", 14), bg="green",
                              command=lambda: on_calculate_button_click(window, p_input, b_input, r_input, g_input, p_prices, b_prices, r_prices, g_prices))
    calculate_button.pack(pady=20)
    window.mainloop()

# Запуск программы
enter_window()
