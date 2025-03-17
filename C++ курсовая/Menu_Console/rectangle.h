#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "figure.h"

class Rectangle : public Figure {
private:
    double x1, y1, x2, y2, x3, y3, x4, y4;
public:
    Rectangle(double x1_, double y1_, double x2_, double y2_,
        double x3_, double y3_, double x4_, double y4_)
        : x1(x1_), y1(y1_), x2(x2_), y2(y2_),
        x3(x3_), y3(y3_), x4(x4_), y4(y4_) {}
public:
    Rectangle(double x1_, double y1_, double x2_, double y2_);
    void Show() const override;
    bool Verification() const override;
    void Move(double dx, double dy) override;
    bool Intersect(const Figure& other) const override;

    // Методы для получения координат вершин
    double GetX1() const { return x1; }
    double GetY1() const { return y1; }
    double GetX2() const { return x2; }
    double GetY2() const { return y2; }
    double GetX3() const { return x3; }
    double GetY3() const { return y3; }
    double GetX4() const { return x4; }
    double GetY4() const { return y4; }

    // Добавленная функция проверки
    bool IsValidRectangle(double x1, double y1, double x2, double y2) const;
};

#endif // RECTANGLE_H

