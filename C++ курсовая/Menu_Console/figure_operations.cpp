#include "figure_operations.h"
#include "rectangle.h"
#include "triangle.h"
#include <iostream>

void CreateTriangle(std::vector<Figure*>& figures) {
    double x1, y1, x2, y2, x3, y3;
    std::cout << "������� ���������� ������ ������������ (x1 y1 x2 y2 x3 y3): ";
    std::cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;

    // ���������, �������� �� ��������� ����������� ��������������
    Triangle tempTriangle(x1, y1, x2, y2, x3, y3);
    if (tempTriangle.Verification()) {
        figures.push_back(new Triangle(x1, y1, x2, y2, x3, y3));
        std::cout << "����������� ������.\n";
    }
    else {
        std::cout << "������: ���������� �� �������� �����������. ����������� �� ������.\n";
    }
}

void CreateRectangle(std::vector<Figure*>& figures) {
    double x1, y1, x2, y2;
    std::cout << "������� ���������� �������������� (x1 y1 x2 y2): ";
    std::cin >> x1 >> y1 >> x2 >> y2;

    // ���������, ��� ���������� �� ����� �� ����� ������
    if (x1 != x2 && y1 != y2) {
        // ���������, �������� �� ��������� ������������� ��������������
        Rectangle tempRectangle(x1, y1, x2, y2);
        if (tempRectangle.Verification()) {
            figures.push_back(new Rectangle(x1, y1, x2, y2));
            std::cout << "������������� ������.\n";
        }
        else {
            std::cout << "������: ���������� �� �������� �������������. ������������� �� ������.\n";
        }
    }
    else {
        std::cout << "������: ���������� ����� �� ����� ������. ������������� �� ������.\n";
    }
}



void DeleteFigure(std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "��� ��������� �����.\n";
        return;
    }
    int index;
    std::cout << "������� ������ ������ ��� ��������: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "�������� ������ ������.\n";
        return;
    }
    delete figures[index];
    figures.erase(figures.begin() + index);
    std::cout << "������ �������.\n";
}

void ShowFigures(const std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "��� ��������� �����.\n";
        return;
    }
    std::cout << "���������� � ���� �������:\n";
    for (size_t i = 0; i < figures.size(); ++i) {
        std::cout << "������ " << i << ":\n"; // ���������� �������� i, ������� � 0
        figures[i]->Show();
        std::cout << std::endl;
    }
}

void VerificationFigure(const std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "��� ��������� �����.\n";
        return;
    }
    int index;
    std::cout << "������� ������ ������ ��� ��������: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "�������� ������ ������.\n";
        return;
    }
    if (figures[index]->Verification()) {
        std::cout << "������ ����������.\n";
    }
    else {
        std::cout << "������ �� ����������.\n";
    }
}

void MoveFigure(std::vector<Figure*>& figures) {
    if (figures.empty()) {
        std::cout << "��� ��������� �����.\n";
        return;
    }
    int index;
    double dx, dy;
    std::cout << "������� ������ ������ ��� �����������: ";
    std::cin >> index;
    if (index < 0 || index >= figures.size()) {
        std::cout << "�������� ������ ������.\n";
        return;
    }
    std::cout << "������� �������� ������ �� x � y: ";
    std::cin >> dx >> dy;
    figures[index]->Move(dx, dy);
    std::cout << "������ ����������.\n";
}

void IntersectFigures(const std::vector<Figure*>& figures) {
    int index1, index2;
    ChooseFigures(figures, index1, index2);
    if (index1 == index2) {
        std::cout << "������� ���������� ������. ����������, �������� ������ ������.\n";
        return;
    }
    if (figures[index1]->Intersect(*figures[index2])) {
        std::cout << "������ ������������.\n";
    }
    else {
        std::cout << "������ �� ������������.\n";
    }
}

void ChooseFigures(const std::vector<Figure*>& figures, int& index1, int& index2) {
    if (figures.size() < 2) {
        std::cout << "��� �������� ����������� ���������� ������� ��� ������� ��� ������.\n";
        return;
    }
    std::cout << "��������� ������:\n";
    for (size_t i = 0; i < figures.size(); ++i) {
        std::cout << i << ". ";
        figures[i]->Show();
        std::cout << std::endl;
    }
    std::cout << "�������� ������� ���� ����� ��� �������� �� �����������: ";
    std::cin >> index1 >> index2;
    if (index1 < 0 || index1 >= figures.size() || index2 < 0 || index2 >= figures.size()) {
        std::cout << "�������� ������� �����.\n";
        return;
    }
}

