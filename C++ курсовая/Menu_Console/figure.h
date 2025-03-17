#ifndef FIGURE_H
#define FIGURE_H

class Figure {
public:
    virtual ~Figure() {}
    virtual void Show() const = 0;
    virtual bool Verification() const = 0;
    virtual void Move(double dx, double dy) = 0;
    virtual bool Intersect(const Figure& other) const = 0;
};

#endif // FIGURE_H
