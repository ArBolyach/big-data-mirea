# Написать программу, которая вычисляет площадь фигуры,
# параметры которой подаются на вход. Фигуры, которые подаются на вход:
# треугольник, прямоугольник, круг. Результатом работы является словарь, где
# ключ – это название фигуры, а значение – это площадь. 

import math

class FigureArea:
    @staticmethod
    def getSquareArea(a:float,b:float)->float:
        return a*b
    
    @staticmethod
    def getTriangleArea(a:float, h:float)->float:
        return (a*h)/2
    
    @staticmethod
    def getCircleArea(r:float)->float:
        return math.pi*(r**2)
    

circleArea:float = FigureArea.getCircleArea(2)
triangleArea:float = FigureArea.getTriangleArea(5,2)
squareArea:float = FigureArea.getSquareArea(10,12)

figureAreas = {
    "площадь круга": circleArea,
    "площадь треугольника": triangleArea,
    "площадь прямоугольника": squareArea
}


print(figureAreas)