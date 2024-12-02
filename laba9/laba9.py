import tkinter as tk
import random

# Глобальные переменные
result_window = game_window = current_player = board = buttons = player_symbol = computer_symbol = None

def check_winner(board, player):# Проверка победителя
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)): return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def game_over(message):
    global result_window
    result_window = tk.Toplevel()
    result_window.title("Конец игры")
    tk.Label(result_window, text=message, font=("Arial", 24)).pack(padx=20, pady=20)
    tk.Button(result_window, text="Новый раунд", command=start_new_game).pack(pady=10)
    tk.Button(result_window, text="Закрыть", command=result_window.quit).pack(pady=10)

def start_new_game():
    game_window.destroy()
    result_window.destroy()
    start_game_window.deiconify()

def start_game_X():# Начало игры для крестиков
    global current_player, board, buttons, player_symbol, computer_symbol, game_window
    board = [["" for _ in range(3)] for _ in range(3)]
    player_symbol, computer_symbol, current_player = "X", "O", "X"
    buttons = [[None for _ in range(3)] for _ in range(3)]
    game_window = tk.Toplevel(start_game_window)
    game_window.title("Крестики-нолики: Игра")
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(game_window, text="", width=10, height=3, font=("Arial", 24), command=lambda i=i, j=j: player_turn(i, j))
            buttons[i][j].grid(row=i, column=j)
    start_game_window.withdraw()

def start_game_O():# Функция для начала игры с ноликами
    global current_player, board, buttons, player_symbol, computer_symbol, game_window
    board = [["" for _ in range(3)] for _ in range(3)]  # Инициализируем поле
    player_symbol = "O"  # Игрок выбирает нолики
    computer_symbol = "X"  # Компьютер будет играть крестиками
    current_player = computer_symbol  # Компьютер ходит первым
    buttons = [[None for _ in range(3)] for _ in range(3)]  # Инициализируем кнопки

    # Создаем игровое окно
    game_window = tk.Toplevel(start_game_window)
    game_window.title("Крестики-нолики: Игра")

    for i in range(3):# Создание кнопок для игрового поля
        for j in range(3):
            buttons[i][j] = tk.Button(game_window, text="", width=10, height=3, font=("Arial", 24),
                                      command=lambda i=i, j=j: player_turn(i, j))
            buttons[i][j].grid(row=i, column=j)

    start_game_window.withdraw()  # Закрыть начальное окно выбора
    computer_turn_first()# После начала игры ходит компьютер первым

def player_turn(i, j):
    global current_player
    if board[i][j] == "":  # Если клетка пуста
        board[i][j] = current_player  # Игрок ставит свой символ
        buttons[i][j].config(text=current_player, state="disabled")  # Отключаем кнопку
        # Проверка на победителя
        if check_winner(board, current_player):
            game_over(f"Игрок ({current_player}) победил!")
            return
        # Проверка на ничью
        if check_draw(board):
            game_over("Ничья!")
            return
        # Переключаем на ход компьютера
        current_player = computer_symbol if current_player == player_symbol else player_symbol
        if current_player == computer_symbol:
            computer_turn()  # Ход компьютера

def computer_turn():# Функция для хода компьютера
    global current_player
    best_move = None
    best_value = float('-inf')

    # Ищем лучший ход для компьютера
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = computer_symbol
                if check_winner(board, computer_symbol):  # Проверка на победу
                    best_move = (i, j)
                    board[i][j] = ""
                    break
                board[i][j] = ""
    if best_move is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player_symbol  # Блокировка хода игрока
                    if check_winner(board, player_symbol):
                        best_move = (i, j)
                        board[i][j] = ""
                        break
                    board[i][j] = ""
    if best_move is None:
        # Если нет блокировки, используем Минимакс
        best_value = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = computer_symbol
                    move_value = minimax(board, 0, False, float('-inf'), float('inf'))
                    board[i][j] = ""
                    if move_value > best_value:
                        best_value = move_value
                        best_move = (i, j)

    # Совершаем лучший ход
    if best_move:
        row, col = best_move
        board[row][col] = computer_symbol
        buttons[row][col].config(text=computer_symbol, state="disabled")  # Отключаем кнопку
    # Проверка на победу
    if check_winner(board, computer_symbol):
        game_over(f"Компьютер ({computer_symbol}) победил!")
        return
    # Проверка на ничью
    if check_draw(board):
        game_over("Ничья!")
        return

    # Теперь ходит игрок
    current_player = player_symbol

def computer_turn_first():# Функция для первого хода компьютера
    global current_player
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    first_move = random.choice(available_moves)  # Выбираем случайную клетку для первого хода
    row, col = first_move
    board[row][col] = computer_symbol
    buttons[row][col].config(text=computer_symbol, state="disabled")  # Отключаем кнопку после первого хода

    current_player = player_symbol  # Теперь ходит игрок

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, computer_symbol): return 1
    if check_winner(board, player_symbol): return -1
    if check_draw(board): return 0
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = computer_symbol
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player_symbol
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha: break
        return min_eval

# Начальное окно выбора
start_game_window = tk.Tk()
start_game_window.title("Выбор игры")
tk.Button(start_game_window, text="Играть за крестики", width=20, height=2, font=("Arial", 14), command=start_game_X).pack(pady=5)
tk.Button(start_game_window, text="Играть за нолики", width=20, height=2, font=("Arial", 14), command=start_game_O).pack(pady=5)
start_game_window.mainloop()
