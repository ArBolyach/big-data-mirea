# Написать программу, которая вычисляет площадь фигуры,
# параметры которой подаются на вход. Фигуры, которые подаются на вход:
# треугольник, прямоугольник, круг. Результатом работы является словарь, где
# ключ – это название фигуры, а значение – это площадь. 

import math

class FigureArea:
    @staticmethod
    def getSquareArea(a:int,b:int)->int:
        return a*b
    
    @staticmethod
    def getTriangleArea(a:int, h:int)->int:
        return (a*h)/2
    
    @staticmethod
    def getCircleArea(r:int)->int:
        return math.pi*(r**2)
    

circleArea:int = FigureArea.getCircleArea(2)
triangleArea:int = FigureArea.getTriangleArea(5,2)
squareArea:int = FigureArea.getSquareArea(10,12)

figureAreas = {
    "площадь круга": circleArea,
    "площадь треугольника": triangleArea,
    "площадь прямоугольника": squareArea
}


print(figureAreas)