# Напишите программу, которая считывает с консоли числа (по
# одному в строке) до тех пор, пока сумма введённых чисел не будет равна 0 и
# после этого выводит сумму квадратов всех считанных чисел.


class Summator:
    def __init__(self):
        self.result = 0
        self.isZero = False
        self._squareResult = 0

    def addNumber(self, num: float):
        self.result += num
        self._squareResult += num**2
        if self.result == 0:
            self.isZero = True

    def getResult(self):
        return self._squareResult


def main():
    summator = Summator()

    while summator.isZero == False:
        summator.addNumber(float(input()))

    print(summator.getResult())


if __name__ == "__main__":
    main()
