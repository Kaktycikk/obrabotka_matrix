#include "geometry_utils.h"
#include <cmath>
#include <algorithm>

bool GeometryUtils::PointInTriangle(double x, double y, double x1, double y1, double x2, double y2, double x3, double y3) {
    double A = 1 / 2 * (-y2 * x3 + y1 * (-x2 + x3) + x1 * (y2 - y3) + x2 * y3);
    double sign = A < 0 ? -1 : 1;
    double s = (y1 * x3 - x1 * y3 + (y3 - y1) * x + (x1 - x3) * y) * sign;
    double t = (x1 * y2 - y1 * x2 + (y1 - y2) * x + (x2 - x1) * y) * sign;

    return s > 0 && t > 0 && (s + t) < 2 * A * sign;
}

// Функция для вычисления ориентации трех точек
int GeometryUtils::Orientation(double x1, double y1, double x2, double y2, double x3, double y3) {
    double val = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2);
    if (val == 0) return 0;  // Точки коллинеарны
    return (val > 0) ? 1 : 2; // 1 - по часовой стрелке, 2 - против часовой стрелки
}

bool GeometryUtils::IntersectSegments(double x1, double y1, double x2, double y2,
    double x3, double y3, double x4, double y4) {
    // Параметры для уравнений прямых, содержащих отрезки
    double a1 = y2 - y1;
    double b1 = x1 - x2;
    double c1 = x1 * (y1 - y2) + y1 * (x2 - x1);

    double a2 = y4 - y3;
    double b2 = x3 - x4;
    double c2 = x3 * (y3 - y4) + y3 * (x4 - x3);

    // Находим точку пересечения прямых
    double det = a1 * b2 - a2 * b1;
    if (det == 0) {
        return false; // Отрезки параллельны
    }
    else {
        double x = (b1 * c2 - b2 * c1) / det;
        double y = (a2 * c1 - a1 * c2) / det;
        // Проверяем, лежит ли точка пересечения внутри отрезков
        return (std::min(x1, x2) <= x && x <= std::max(x1, x2) &&
            std::min(y1, y2) <= y && y <= std::max(y1, y2) &&
            std::min(x3, x4) <= x && x <= std::max(x3, x4) &&
            std::min(y3, y4) <= y && y <= std::max(y3, y4));
    }
}

// Функция для определения, лежит ли точка (pX, pY) на отрезке (x1, y1) - (x2, y2)
bool OnSegment(double x1, double y1, double x2, double y2, double pX, double pY) {
    if (pX <= std::max(x1, x2) && pX >= std::min(x1, x2) &&
        pY <= std::max(y1, y2) && pY >= std::min(y1, y2))
        return true;

    return false;
}

