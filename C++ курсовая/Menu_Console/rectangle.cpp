#include "rectangle.h"
#include "triangle.h"
#include <iostream>

Rectangle::Rectangle(double x1, double y1, double x2, double y2) : x1(x1), y1(y1), x2(x2), y2(y2) {}

void Rectangle::Show() const {
    std::cout << "������������� � ������������ (" << x1 << ", " << y1 << ") � (" << x2 << ", " << y2 << ")\n";
}

bool Rectangle::Verification() const {
    return IsValidRectangle(x1, y1, x2, y2);
}



// ���������� ������� Move
void Rectangle::Move(double dx, double dy) {
    x1 += dx;
    y1+= dy;
}

bool Rectangle::Intersect(const Figure& other) const {
    // ���� ���������� ����� ���������, ������� �� ���������������
    if (this == &other) {
        return true;
    }

    // ���������, �������� �� ������ ������ ���������������
    const Rectangle* other_rectangle = dynamic_cast<const Rectangle*>(&other);
    if (other_rectangle) {
        // ���������, ������������ �� �������������� �� �������� ��� ������
        // ���� ��� ����� ��������, ���� ����� ����� ������ ����������� �����������
        return (x1 <= other_rectangle->x2 && x2 >= other_rectangle->x1 &&
            y1 <= other_rectangle->y2 && y2 >= other_rectangle->y1);
    }

    // ���� �� ����������� �� ���� �� ������� ����, ������� ������ �� ���������������
    return false;
}

// ���������� ������� �������� ��������������
bool Rectangle::IsValidRectangle(double x1_, double y1_, double x2_, double y2_) const {
    // ���������, ��� ��� ������ ����� �� ���������
    if (x1_ == x2_ && y1_ == y2_) {
        std::cout << "��� ������� �������������� ���������, ��� �� �������������!\n";
        return false;
    }

    // ���������, ��� �� ��� ����� ����� �� ����� ������
    if ((x1_ == x2_ && x1_ == x2_ && x1_ == x2_) || (y1_ == y2_ && y1_ == y2_ && y1_ == y2_)) {
        std::cout << "��� ������� �������������� ����� �� ����� ������, ��� �� �������������!\n";
        return false;
    }

    return true;
}

