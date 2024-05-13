"""
имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |

lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...

1. Реализовать сбор уникальных записей
2. Случается, что под одинаковым id присутствуют разные данные - собрать такие записи
"""

import pandas as pd
from pandas import DataFrame


def read_data(filename: str, sep: str) -> DataFrame:
    """
    На вход подается путь к файлу и разделитель
    Записи с повторяющимися идентификаторы объединил в массив
    """
    df = pd.read_csv(filename, sep=sep)
    df_count = df["id"].value_counts()
    df_value = df[df["id"].isin(df_count[df_count > 1].index)]
    df_uniq = df[df["id"].isin(df_count[df_count <= 1].index)]
    df_unioned = df_value.groupby(by="id", as_index=False).agg(list)

    return pd.concat([df_uniq, df_unioned], ignore_index=True)


if __name__ == "__main__":
    res = read_data("./tasks/task1/data.csv", "|")
    counts = res["id"].value_counts()
    print(res)
    assert sum(counts) == res.shape[0], "Есть не уникальные идентификаторы"
