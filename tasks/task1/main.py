import pandas as pd
from pandas import DataFrame


def read_data(filename: str, sep: str) -> DataFrame:
    df = pd.read_csv(filename, sep=sep)
    df_count = df["id"].value_counts()
    
    df_value = df[df["id"].isin(df_count[df_count > 1].index)]
    df_uniq = df[df["id"].isin(df_count[df_count <= 1].index)]
    df_unioned = df_value.groupby(by="id", as_index=False).agg(list)

    res = pd.concat([df_uniq, df_unioned], ignore_index=True)

    return res


if __name__ == "__main__":
    res = read_data("./tasks/task1/data.csv", "|")
    counts = res["id"].value_counts()
    assert sum(counts) == res.shape[0], "Есть не уникальные идентификаторы"
    
