def process_file(fileName):
    hex_digits, max_value = "0123456789ABCDEF", 4096
    matching_count = total_count = 0
    min_number = None
    current_number = ""

    with open(fileName, 'r') as file:
        while True:
            char = file.read(1).upper()
            if not char or char == " ":
                if current_number:
                    total_count += 1
                    if current_number.startswith("A") and all(c in hex_digits for c in current_number):
                        decimal_value = int(current_number, 16)
                        if decimal_value <= max_value and decimal_value % 2 != 0:
                            matching_count += 1
                            min_number = decimal_value if min_number is None else min(min_number, decimal_value)
                if not char: break
                current_number = ""
            else:
                current_number += char  # Собираем число посимвольно

    percentage = (matching_count / total_count * 100) if total_count else 0
    print(f"Процентное содержание таких чисел: {percentage:.2f}%")
    if min_number is not None:
        print("Минимальное число:", min_number)
        print("Минимальное число прописью:", ' '.join(
            "ноль один два три четыре пять шесть семь восемь девять".split()[int(d)] for d in str(min_number)
        ))

fileName = 'text.txt'
process_file(fileName)
