"""
в наличии список множеств. внутри множества целые числа
посчитать 
1. общее количество чисел
2. общую сумму чисел
3. посчитать среднее значение
4. собрать все числа из множеств в один кортеж
"""

from typing import List


def calculate_set(a: List[set]) -> dict:
    """
    Выполняется расчет для задания.
    На выходе будут все необходимые параметры
    """
    cnt = sum(len(s) for s in a)
    sum_number = sum(sum(s) for s in a)
    average = sum_number / cnt
    tuple_number = tuple(s for elem in a for s in elem)
    return {
        "count_number": cnt,
        "sum_number": sum_number,
        "average_number": average,
        "tuple_number": tuple_number,
    }


if __name__ == "__main__":
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
    ans = calculate_set(m)
    print(ans)
