#ifndef FIGURE_OPERATIONS_H
#define FIGURE_OPERATIONS_H

#include <iostream>
#include <vector>
#include "triangle.h"
#include "rectangle.h"

	// Функции для операций с фигурами
	void CreateTriangle(std::vector<Figure*>& figures);
	void CreateRectangle(std::vector<Figure*>& figures);
	void DeleteFigure(std::vector<Figure*>& figures);
	void ShowFigures(const std::vector<Figure*>& figures);
	void VerificationFigure(const std::vector<Figure*>& figures);
	void MoveFigure(std::vector<Figure*>& figures);
	void IntersectFigures(const std::vector<Figure*>& figures);
	void ChooseFigures(const std::vector<Figure*>& figures, int& index1, int& index2);

#endif // FIGURE_OPERATIONS_H
