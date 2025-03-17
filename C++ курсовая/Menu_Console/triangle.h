#ifndef TRIANGLE_H
#define TRIANGLE_H

#include "figure.h"
#include "Point.h"

class Triangle : public Figure {
private:
    double x1, y1, x2, y2, x3, y3;

public:
    Triangle(double x1, double y1, double x2, double y2, double x3, double y3);
    void Show() const override;
    bool Verification() const override;
    void Move(double dx, double dy) override;
    bool Intersect(const Figure& other) const override;

    bool IsValidTriangle(double x1, double y1, double x2, double y2, double x3, double y3) const;

    // Методы получения координат точек
    double GetX1() const { return x1; }
    double GetY1() const { return y1; }
    double GetX2() const { return x2; }
    double GetY2() const { return y2; }
    double GetX3() const { return x3; }
    double GetY3() const { return y3; }

private:
    bool ContainsVertex(double x, double y) const;
};
#endif // TRIANGLE_H