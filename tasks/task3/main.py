"""
имеется список списков
a = [[1,2,3], [4,5,6]]
cделать список словарей
b = [{'k1': 1, 'k2': 2, 'k3':3}, {'k1': 4, 'k2': 5, 'k3': 6}]
написать решение в одну строку
"""

from typing import List


def refactor_array(arr: List[list]) -> List[dict]:
    """
    Решение в одну строку
    """
    res = list(map(lambda x: {f"k{index+1}": value for index, value in enumerate(x)}, arr))
    return res


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    ans = refactor_array(a)
    print(ans)
