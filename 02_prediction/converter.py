from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    enumerated = enumerate(values)
    my_dict = {item: index for index, item in enumerated}
    return my_dict


def columns_mapper(columns_str: list[str], df: pd.DataFrame) -> dict[str, dict[str, int]]:
    mapper = {}
    for item in columns_str:
        col = df[item]
        unq = col.unique()
        unq = enumerator(unq)
        mapper[item] = unq
    return mapper

def convert_x(df: pd.DataFrame, mapper: dict[str, dict[str, int]]) -> pd.DataFrame:
    converted = df.copy()
    for col  in mapper:
        converted[col] = converted[col].map(mapper[col])
    return converted





# df = pd.DataFrame({
#     "Company": ["Toyota", "Toyota", "Hundai"],
#     "Model": ["Camry", "Corolla", "i10"]
# })
#
# print('Enumerator !!!', enumerator(['Toyota','BMW','Opel']))
#
# mapper = columns_mapper(["Company", "Model"], df)
# print('columns_mapper!!!',mapper)
#
#
# converted = convert_x(df, mapper)
#
# print('converted!!!         ',converted)