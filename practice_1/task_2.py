# Написать программу, которая на вход получает два числа и
# операцию, которую к ним нужно применить. Должны быть реализованы
# следующие операции: +, -, /, //, abs – модуль, pow или ** – возведение в
# степень.

from enum import Enum


class Calculator(Enum):
    SUM = "+"
    SUB = "-"
    DIV = "/"
    DIV_INTEGER = "//"
    ABS = "abs"
    POW = "pow"

    @staticmethod
    def sum(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def sub(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def div(a: float, b: float) -> float:
        return a / b

    @staticmethod
    def div_integer(a: float, b: float) -> float:
        return a // b

    @staticmethod
    def abs(a: float) -> float:
        return abs(a)

    @staticmethod
    def pow(a: float, b: float) -> float:
        return a**b


def main():
    a, b, symbol, result = float(input()), float(input()), input(), 0

    match symbol:
        case Calculator.SUM.value:
            result = Calculator.sum(a, b)
        case Calculator.SUB.value:
            result = Calculator.sub(a, b)
        case Calculator.DIV.value:
            result = Calculator.div(a, b)
        case Calculator.DIV_INTEGER.value:
            result = Calculator.div_integer(a, b)
        case Calculator.ABS.value:
            result = Calculator.abs(a)
        case Calculator.POW.value:
            result = Calculator.pow(a, b)
        case _:
            raise ValueError("Неизвестная команда")

    print(result)


if __name__ == "__main__":
    main()
