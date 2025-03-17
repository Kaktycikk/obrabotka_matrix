#include "triangle.h"
#include"geometry_utils.h"
#include "Point.h"
#include "rectangle.h"
#include <iostream>
#include <cmath>

Triangle::Triangle(double x1_, double y1_, double x2_, double y2_, double x3_, double y3_)
    : x1(x1_), y1(y1_), x2(x2_), y2(y2_), x3(x3_), y3(y3_) {}

void Triangle::Show() const {
    std::cout << "Треугольник с вершинами: ";
    std::cout << "(" << x1 << ", " << y1 << "), ";
    std::cout << "(" << x2 << ", " << y2 << "), ";
    std::cout << "(" << x3 << ", " << y3 << ")" << std::endl;
}

bool Triangle::Verification() const {
    // Проверяем, что вершины треугольника не лежат на одной прямой
    return IsValidTriangle(x1, y1, x2, y2, x3, y3);
}

void Triangle::Move(double dx, double dy) {
    // Перемещаем каждую вершину на величину dx и dy
    x1 += dx;
    y1 += dy;
    x2 += dx;
    y2 += dy;
    x3 += dx;
    y3 += dy;
}

bool Triangle::ContainsVertex(double x, double y) const {
    // Проверяем, лежит ли точка (x, y) внутри треугольника
    double A = 1 / 2 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3);
    double sign = A < 0 ? -1 : 1;
    double s = (y1 * x3 - x1 * y3 + (y3 - y1) * x + (x1 - x3) * y) * sign;
    double t = (x1 * y2 - y1 * x2 + (y1 - y2) * x + (x2 - x1) * y) * sign;

    return s > 0 && t > 0 && (s + t) < 2 * A * sign;
}

bool Triangle::Intersect(const Figure& other) const {
    // Проверяем, является ли другая фигура также треугольником
    const Triangle* other_triangle = dynamic_cast<const Triangle*>(&other);
    if (other_triangle) {
        // Проверяем, имеют ли треугольники общие вершины
        if (ContainsVertex(other_triangle->x1, other_triangle->y1) ||
            ContainsVertex(other_triangle->x2, other_triangle->y2) ||
            ContainsVertex(other_triangle->x3, other_triangle->y3)) {
            return true;
        }

        // Проверяем пересечение сторон одного треугольника с другим
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
    // Если ни одно из условий не выполнено, считаем треугольники не пересекающимися
    return false;
}

bool Triangle::IsValidTriangle(double x1_, double y1_, double x2_, double y2_, double x3_, double y3_) const {
    // Проверяем, что все три точки не лежат на одной прямой
    if ((x1_ * (y2_ - y3_) + x2_ * (y3_ - y1_) + x3_ * (y1_ - y2_)) == 0) {
        std::cout << "Точки лежат на одной прямой, не могут образовать треугольник!\n";
        return false;
    }

    // Проверяем, что все три точки не совпадают
    if (x1_ == x2_ && y1_ == y2_ && x1_ == x3_ && y1_ == y3_) {
        std::cout << "Все вершины треугольника совпадают, это не треугольник!\n";
        return false;
    }
    else if (x1_ == x2_ && y1_ == y2_ || x1_ == x3_ && y1_ == y3_ || x2_ == x3_ && y2_ == y3_) {
        std::cout << "Две вершины треугольника совпадают, это не треугольник!\n";
        return false;
    }

    return true;
}


