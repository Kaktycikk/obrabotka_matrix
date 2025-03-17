#include <iostream>
#include <vector>
#include "figure_operations.h"
#include "triangle.h"

int main() {
    setlocale(LC_ALL, "Russian");

    std::vector<Figure*> figures;

    int choice;
    do {
        std::cout << "Меню:\n";
        std::cout << "1. Создать треугольник\n";
        std::cout << "2. Создать прямоугольник\n";
        std::cout << "3. Удалить фигуру\n";
        std::cout << "4. Показать информацию о всех фигурах\n";
        std::cout << "5. Проверить существование фигуры\n";
        std::cout << "6. Переместить фигуру\n";
        std::cout << "7. Проверить пересечение фигур\n";
        std::cout << "8. Выйти из программы\n";
        std::cout << "Выберите действие: ";
        std::cin >> choice;

        switch (choice) {
        case 1:
            CreateTriangle(figures);
            break;
        case 2:
            CreateRectangle(figures);
            break;
        case 3:
            DeleteFigure(figures);
            break;
        case 4:
            ShowFigures(figures);
            break;
        case 5:
            VerificationFigure(figures);
            break;
        case 6:
            MoveFigure(figures);
            break;
        case 7:
            IntersectFigures(figures);
            break;
        case 8:
            std::cout << "Программа завершена.\n";
            break;
        default:
            std::cout << "Неверный выбор. Пожалуйста, выберите существующее действие.\n";
            break;
        }
    } while (choice != 0);

    // Очистка памяти
    for (Figure* figure : figures) {
        delete figure;
    }

    return 0;
}


