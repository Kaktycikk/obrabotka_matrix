#include "triangle.h"
#include"geometry_utils.h"
#include "Point.h"
#include "rectangle.h"
#include <iostream>
#include <cmath>

Triangle::Triangle(double x1_, double y1_, double x2_, double y2_, double x3_, double y3_)
    : x1(x1_), y1(y1_), x2(x2_), y2(y2_), x3(x3_), y3(y3_) {}

void Triangle::Show() const {
    std::cout << "����������� � ���������: ";
    std::cout << "(" << x1 << ", " << y1 << "), ";
    std::cout << "(" << x2 << ", " << y2 << "), ";
    std::cout << "(" << x3 << ", " << y3 << ")" << std::endl;
}

bool Triangle::Verification() const {
    // ���������, ��� ������� ������������ �� ����� �� ����� ������
    return IsValidTriangle(x1, y1, x2, y2, x3, y3);
}

void Triangle::Move(double dx, double dy) {
    // ���������� ������ ������� �� �������� dx � dy
    x1 += dx;
    y1 += dy;
    x2 += dx;
    y2 += dy;
    x3 += dx;
    y3 += dy;
}

bool Triangle::ContainsVertex(double x, double y) const {
    // ���������, ����� �� ����� (x, y) ������ ������������
    double A = 1 / 2 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3);
    double sign = A < 0 ? -1 : 1;
    double s = (y1 * x3 - x1 * y3 + (y3 - y1) * x + (x1 - x3) * y) * sign;
    double t = (x1 * y2 - y1 * x2 + (y1 - y2) * x + (x2 - x1) * y) * sign;

    return s > 0 && t > 0 && (s + t) < 2 * A * sign;
}

bool Triangle::Intersect(const Figure& other) const {
    // ���������, �������� �� ������ ������ ����� �������������
    const Triangle* other_triangle = dynamic_cast<const Triangle*>(&other);
    if (other_triangle) {
        // ���������, ����� �� ������������ ����� �������
        if (ContainsVertex(other_triangle->x1, other_triangle->y1) ||
            ContainsVertex(other_triangle->x2, other_triangle->y2) ||
            ContainsVertex(other_triangle->x3, other_triangle->y3)) {
            return true;
        }

        // ��������� ����������� ������ ������ ������������ � ������
        if (GeometryUtils::IntersectSegments(x1, y1, x2, y2, other_triangle->x1, other_triangle->y1, other_triangle->x2, other_triangle->y2) ||
            GeometryUtils::IntersectSegments(x1, y1, x2, y2, other_triangle->x2, other_triangle->y2, other_triangle->x3, other_triangle->y3) ||
            GeometryUtils::IntersectSegments(x1, y1, x2, y2, other_triangle->x3, other_triangle->y3, other_triangle->x1, other_triangle->y1) ||
            GeometryUtils::IntersectSegments(x2, y2, x3, y3, other_triangle->x1, other_triangle->y1, other_triangle->x2, other_triangle->y2) ||
            GeometryUtils::IntersectSegments(x2, y2, x3, y3, other_triangle->x2, other_triangle->y2, other_triangle->x3, other_triangle->y3) ||
            GeometryUtils::IntersectSegments(x2, y2, x3, y3, other_triangle->x3, other_triangle->y3, other_triangle->x1, other_triangle->y1) ||
            GeometryUtils::IntersectSegments(x3, y3, x1, y1, other_triangle->x1, other_triangle->y1, other_triangle->x2, other_triangle->y2) ||
            GeometryUtils::IntersectSegments(x3, y3, x1, y1, other_triangle->x2, other_triangle->y2, other_triangle->x3, other_triangle->y3) ||
            GeometryUtils::IntersectSegments(x3, y3, x1, y1, other_triangle->x3, other_triangle->y3, other_triangle->x1, other_triangle->y1)) {
            return true;
        }
    }
    // ���� �� ���� �� ������� �� ���������, ������� ������������ �� ���������������
    return false;
}

bool Triangle::IsValidTriangle(double x1_, double y1_, double x2_, double y2_, double x3_, double y3_) const {
    // ���������, ��� ��� ��� ����� �� ����� �� ����� ������
    if ((x1_ * (y2_ - y3_) + x2_ * (y3_ - y1_) + x3_ * (y1_ - y2_)) == 0) {
        std::cout << "����� ����� �� ����� ������, �� ����� ���������� �����������!\n";
        return false;
    }

    // ���������, ��� ��� ��� ����� �� ���������
    if (x1_ == x2_ && y1_ == y2_ && x1_ == x3_ && y1_ == y3_) {
        std::cout << "��� ������� ������������ ���������, ��� �� �����������!\n";
        return false;
    }
    else if (x1_ == x2_ && y1_ == y2_ || x1_ == x3_ && y1_ == y3_ || x2_ == x3_ && y2_ == y3_) {
        std::cout << "��� ������� ������������ ���������, ��� �� �����������!\n";
        return false;
    }

    return true;
}


