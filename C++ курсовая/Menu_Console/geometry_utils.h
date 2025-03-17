#ifndef GEOMETRY_UTILS_H
#define GEOMETRY_UTILS_H

class GeometryUtils {
public:
    static bool PointInTriangle(double x, double y, double x1, double y1, double x2, double y2, double x3, double y3);
    static bool IntersectSegments(double x1, double y1, double x2, double y2,
        double x3, double y3, double x4, double y4);
    static int Orientation(double x1, double y1, double x2, double y2, double x3, double y3);
};

#endif // GEOMETRY_UTILS_H