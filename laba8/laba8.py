import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import matplotlib.pyplot as plt


class Tariff:
    def __init__(self, name, service_type, customer):
        self.name = name
        self.service_type = service_type
        self.customer = customer


class TariffsManager:
    def __init__(self):
        self.tariffs = []

    def load_from_file(self, filename):
        """Загрузка тарифов из файла"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            for line in lines:
                name, service_type, customer = line.strip().split(',')
                self.tariffs.append(Tariff(name, service_type, customer))
        except UnicodeDecodeError:
            try:
                with open(filename, 'r', encoding='windows-1251') as file:
                    lines = file.readlines()
                for line in lines:
                    name, service_type, customer = line.strip().split(',')
                    self.tariffs.append(Tariff(name, service_type, customer))
            except Exception as e:
                messagebox.showwarning("Ошибка", f"Ошибка при чтении файла: {e}")
        except FileNotFoundError:
            messagebox.showwarning("Ошибка", "Файл не найден.")
        except Exception as e:
            messagebox.showwarning("Ошибка", f"Ошибка при чтении файла: {e}")

    def segment_by_customer(self):
        """Сегментация тарифов по заказчикам"""
        customer_dict = {}
        for tariff in self.tariffs:
            if tariff.customer in customer_dict:
                customer_dict[tariff.customer] += 1
            else:
                customer_dict[tariff.customer] = 1
        return customer_dict

    def segment_by_service_type(self):
        """Сегментация тарифов по типу услуги"""
        service_dict = {}
        for tariff in self.tariffs:
            if tariff.service_type in service_dict:
                service_dict[tariff.service_type] += 1
            else:
                service_dict[tariff.service_type] = 1
        return service_dict

    def visualize_segmentation(self, data, title):
        """Визуализация сегментации в виде круговой диаграммы"""
        labels = list(data.keys())
        sizes = list(data.values())
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(title)
        plt.show()


def load_tariffs_gui(manager):
    """Графический интерфейс для загрузки данных из файла"""
    filename = filedialog.askopenfilename(title="Выберите файл с тарифами", filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")))
    if filename:
        manager.load_from_file(filename)
        messagebox.showinfo("Успех", "Тарифы успешно загружены.")


def show_customer_segmentation(manager):
    """Графический интерфейс для отображения сегментации по заказчикам"""
    customer_data = manager.segment_by_customer()
    manager.visualize_segmentation(customer_data, "Сегментация по заказчикам")


def show_service_type_segmentation(manager):
    """Графический интерфейс для отображения сегментации по типам услуг"""
    service_data = manager.segment_by_service_type()
    manager.visualize_segmentation(service_data, "Сегментация по типам услуг")


def main_gui():
    """Основной графический интерфейс"""
    manager = TariffsManager()

    window = tk.Tk()
    window.title("Меню")

    # Устанавливаем размер окна
    window.geometry("400x300")  # Размер окна (ширина x высота)

    # Центрируем окно на экране
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

    # Кнопки интерфейса
    load_button = tk.Button(window, text="Загрузить тарифы", command=lambda: load_tariffs_gui(manager))
    load_button.pack(pady=20)

    segment_customer_button = tk.Button(window, text="Сегментация по заказчикам",
                                        command=lambda: show_customer_segmentation(manager))
    segment_customer_button.pack(pady=10)

    segment_service_button = tk.Button(window, text="Сегментация по типам услуг",
                                       command=lambda: show_service_type_segmentation(manager))
    segment_service_button.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main_gui()
