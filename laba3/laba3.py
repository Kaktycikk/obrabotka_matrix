# Шестнадцатеричные нечетные числа, не превышающие 409610 и начинающиеся с «А». Отдельно
# вывести их процентное содержание в файле. Минимальное число вывести прописью.
def is_valid_hex_number(num_str):
    """Проверяет, является ли строка шестнадцатеричным нечётным числом, начинающимся с 'А' и не превышающим 4096."""
    try:
        if num_str.startswith('-'):
            num_str = num_str[1:]  
        if not num_str.startswith('A') or not all(c in '0123456789ABCDEF' for c in num_str):
            return False
        decimal_value = int(num_str, 16)  
        return abs(decimal_value) % 2 != 0 and abs(decimal_value) <= 0x1000
    except ValueError:
        return False


def convert_to_words_hex(num_str):
    """Преобразует шестнадцатеричное число в пропись."""
    digit_to_word_hex = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять',
        'A': 'десять', 'B': 'одиннадцать', 'C': 'двенадцать', 'D': 'тринадцать',
        'E': 'четырнадцать', 'F': 'пятнадцать'
    }
    sign = "минус " if num_str.startswith('-') else ""
    num_str = num_str.lstrip('-')
    return sign + ' '.join(digit_to_word_hex[char.upper()] for char in num_str if char.upper() in digit_to_word_hex)


def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().split()
        hex_numbers = [obj for obj in content if is_valid_hex_number(obj)]

        total_objects = len(content)
        if total_objects > 0:
            percentage = (len(hex_numbers) / total_objects) * 100
            print(f"Процентное содержание шестнадцатеричных нечетных чисел: {percentage:.2f}%")
            print("Числа, соответствующие критериям: ", ' '.join(hex_numbers))
        else:
            print("Файл пуст или не содержит объектов.")

        if hex_numbers:
            min_hex = min(hex_numbers, key=lambda x: int(x, 16))
            print(f"Минимальное число: {min_hex} ({convert_to_words_hex(min_hex)})")
        else:
            print("Шестнадцатеричные числа, соответствующие критериям, не найдены.")


filename = 'input.txt'  
process_file(filename)



