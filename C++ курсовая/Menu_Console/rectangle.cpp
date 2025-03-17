#include "rectangle.h"
#include "triangle.h"
#include <iostream>

Rectangle::Rectangle(double x1, double y1, double x2, double y2) : x1(x1), y1(y1), x2(x2), y2(y2) {}

void Rectangle::Show() const {
    std::cout << "Прямоугольник с координатами (" << x1 << ", " << y1 << ") и (" << x2 << ", " << y2 << ")\n";
}

bool Rectangle::Verification() const {
    return IsValidRectangle(x1, y1, x2, y2);
}



// Реализация функции Move
void Rectangle::Move(double dx, double dy) {
    x1 += dx;
    y1+= dy;
}

bool Rectangle::Intersect(const Figure& other) const {
    // Если координаты фигур совпадают, считаем их пересекающимися
    if (this == &other) {
        return true;
    }

    // Проверяем, является ли другая фигура прямоугольником
    const Rectangle* other_rectangle = dynamic_cast<const Rectangle*>(&other);
    if (other_rectangle) {
        // Проверяем, пересекаются ли прямоугольники по границам или внутри
        // Этот код можно изменить, если нужно более точное определение пересечения
        return (x1 <= other_rectangle->x2 && x2 >= other_rectangle->x1 &&
            y1 <= other_rectangle->y2 && y2 >= other_rectangle->y1);
    }

    // Если не выполнилось ни одно из условий выше, считаем фигуры не пересекающимися
    return false;
}

// Реализация функции проверки прямоугольника
bool Rectangle::IsValidRectangle(double x1_, double y1_, double x2_, double y2_) const {
    // Проверяем, что все четыре точки не совпадают
    if (x1_ == x2_ && y1_ == y2_) {
        std::cout << "Все вершины прямоугольника совпадают, это не прямоугольник!\n";
        return false;
    }

    // Проверяем, что не все точки лежат на одной прямой
    if ((x1_ == x2_ && x1_ == x2_ && x1_ == x2_) || (y1_ == y2_ && y1_ == y2_ && y1_ == y2_)) {
        std::cout << "Все вершины прямоугольника лежат на одной прямой, это не прямоугольник!\n";
        return false;
    }

    return true;
}

