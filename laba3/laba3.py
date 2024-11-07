# Программа для чтения символов из файла, распознавания и преобразования объектов по заданному правилу

def is_valid_hex_number(num_str):
    """Проверяет, является ли строка шестнадцатеричным нечётным числом, начинающимся с 'А' и не превышающим 4096."""
    try:
        if not num_str.startswith('A'):
            return False
        decimal_value = int(num_str, 16)
        # Проверка, что число нечётное и не превышает 4096
        return decimal_value % 2 != 0 and decimal_value <= 0x1000
    except ValueError:
        return False


def convert_to_words(num):
    """Преобразует число в последовательный вывод всех его цифр прописью."""
    digit_to_word = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digit_to_word[digit] for digit in str(num))


def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        objects = content.split()  # Разделение объектов без использования регулярных выражений
        hex_numbers = [obj for obj in objects if is_valid_hex_number(obj)]

        total_objects = len(objects)
        if total_objects > 0:
            percentage = (len(hex_numbers) / total_objects) * 100
            print(f"Процентное содержание шестнадцатеричных нечетных чисел: {percentage:.2f}%")
            print("Числа, соответствующие критериям: ", ' '.join(hex_numbers))
        else:
            print("Файл пуст или не содержит объектов.")

        if hex_numbers:
            min_hex = min(hex_numbers, key=lambda x: int(x, 16))
            print(f"Минимальное число: {min_hex} ({convert_to_words(int(min_hex, 16))})")
        else:
            print("Шестнадцатеричные числа, соответствующие критериям, не найдены.")


# Пример использования
filename = 'input.txt'  # Убедитесь, что файл 'input.txt' существует и содержит тестовые данные
process_file(filename)

