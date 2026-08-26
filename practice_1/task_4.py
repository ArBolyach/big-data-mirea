# Напишите программу, которая выводит последовательность
# чисел, длинною N, где каждое число повторяется столько раз, чему оно равно.
# На вход программе передаётся неотрицательное целое число N. Например,
# если N = 7, то программа должна вывести 1 2 2 3 3 3 4. Вывод элементов списка
# через пробел – print(*list).

a = int(input())

def generateSequence(n:int):
    result = []
    for i in range(n):
        for _ in range(i):
            if (len(result) == n):
                return result
            result.append(i)

print(*generateSequence(a))