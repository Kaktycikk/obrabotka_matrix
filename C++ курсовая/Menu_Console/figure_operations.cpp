#include "figure_operations.h"
#include "rectangle.h"
#include "triangle.h"
#include <iostream>

void CreateTriangle(std::vector<Figure*>& figures) {
    double x1, y1, x2, y2, x3, y3;
    std::cout << "Введите координаты вершин треугольника (x1 y1 x2 y2 x3 y3): ";
    std::cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // Проверяем, является ли введенный треугольник действительным
    Triangle tempTriangle(x1, y1, x2, y2, x3, y3);
    if (tempTriangle.Verification()) {
        figures.push_back(new Triangle(x1, y1, x2, y2, x3, y3));
        std::cout << "Треугольник создан.\n";
    }
    else {
        std::cout << "Ошибка: координаты не образуют треугольник. Треугольник не создан.\n";
    }
}

void CreateRectangle(std::vector<Figure*>& figures) {
    double x1, y1, x2, y2;
    std::cout << "Введите координаты прямоугольника (x1 y1 x2 y2): ";
    std::cin >> x1 >> y1 >> x2 >> y2;

    // Проверяем, что координаты не лежат на одной прямой
    if (x1 != x2 && y1 != y2) {
        // Проверяем, является ли введенный прямоугольник действительным
        Rectangle tempRectangle(x1, y1, x2, y2);
        if (tempRectangle.Verification()) {
            figures.push_back(new Rectangle(x1, y1, x2, y2));
            std::cout << "Прямоугольник создан.\n";
        }
        else {
            std::cout << "Ошибка: координаты не образуют прямоугольник. Прямоугольник не создан.\n";
        }
    }
    else {
        std::cout << "Ошибка: координаты лежат на одной прямой. Прямоугольник не создан.\n";
    }
}



void DeleteFigure(std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "Нет созданных фигур.\n";
        return;
    }
    int index;
    std::cout << "Введите индекс фигуры для удаления: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "Неверный индекс фигуры.\n";
        return;
    }
    delete figures[index];
    figures.erase(figures.begin() + index);
    std::cout << "Фигура удалена.\n";
}

void ShowFigures(const std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "Нет созданных фигур.\n";
        return;
    }
    std::cout << "Информация о всех фигурах:\n";
    for (size_t i = 0; i < figures.size(); ++i) {
        std::cout << "Фигура " << i << ":\n"; // Используем значение i, начиная с 0
        figures[i]->Show();
        std::cout << std::endl;
    }
}

void VerificationFigure(const std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "Нет созданных фигур.\n";
        return;
    }
    int index;
    std::cout << "Введите индекс фигуры для проверки: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "Неверный индекс фигуры.\n";
        return;
    }
    if (figures[index]->Verification()) {
        std::cout << "Фигура существует.\n";
    }
    else {
        std::cout << "Фигура не существует.\n";
    }
}

void MoveFigure(std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "Нет созданных фигур.\n";
        return;
    }
    int index;
    double dx, dy;
    std::cout << "Введите индекс фигуры для перемещения: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "Неверный индекс фигуры.\n";
        return;
    }
    std::cout << "Введите величину сдвига по x и y: ";
    std::cin >> dx >> dy;
    figures[index]->Move(dx, dy);
    std::cout << "Фигура перемещена.\n";
}

void IntersectFigures(const std::vector<Figure*>& figures) {
    int index1, index2;
    ChooseFigures(figures, index1, index2);
    if (index1 == index2) {
        std::cout << "Выбраны одинаковые фигуры. Пожалуйста, выберите разные фигуры.\n";
        return;
    }
    if (figures[index1]->Intersect(*figures[index2])) {
        std::cout << "Фигуры пересекаются.\n";
    }
    else {
        std::cout << "Фигуры не пересекаются.\n";
    }
}

void ChooseFigures(const std::vector<Figure*>& figures, int& index1, int& index2) {
    if (figures.size() < 2) {
        std::cout << "Для проверки пересечения необходимо создать как минимум две фигуры.\n";
        return;
    }
    std::cout << "Доступные фигуры:\n";
    for (size_t i = 0; i < figures.size(); ++i) {
        std::cout << i << ". ";
        figures[i]->Show();
        std::cout << std::endl;
    }
    std::cout << "Выберите индексы двух фигур для проверки их пересечения: ";
    std::cin >> index1 >> index2;
    if (index1 < 0 || index1 >= figures.size() || index2 < 0 || index2 >= figures.size()) {
        std::cout << "Неверные индексы фигур.\n";
        return;
    }
}

