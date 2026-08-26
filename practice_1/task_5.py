# Даны два списка:
# А = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
# В = [‘a’, ’b’, ’c’, ’c’, ’c’, ’b’, ’a’, ’c’, ’a’, ’a’, ’b’, ’c’, ’b’, ’a’]
# Создать словарь, в котором ключи – это содержимое списка В, а
# значения для ключей словаря – это сумма всех элементов списка А в
# соответствии с буквой, содержащийся на той же позиции в списке В.
# Пример результата программы: {‘a’ : 10, ‘b’ : 15, ‘c’ : 6}.


def solveSequence(array_1, array_2):
    array_len: int = len(array_1)
    result = {}
    for i in range(array_len):
        if array_2[i] in result:
            result[array_2[i]] = result.get(array_2[i]) + array_1[i]
        else:
            result[array_2[i]] = array_1[i]
    return result


a1 = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
a2 = ["a", "b", "c", "c", "c", "b", "a", "c", "a", "a", "b", "c", "b", "a"]

print(solveSequence(a1, a2))
