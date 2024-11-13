import pandas as pd
import numpy as np


def dataframe_to_dict_list(df, columns):
    """
    将DataFrame的指定列转换为字典的列表。
    
    参数:
    df -- pandas DataFrame对象
    columns -- 需要转换的列名列表
    
    返回:
    一个字典的列表，每个字典代表DataFrame中的一行。
    """
    # 确保所有列名都在DataFrame中
    if not all(col in df.columns for col in columns):
        raise ValueError("Some columns are not present in the DataFrame")
    
    # 使用DataFrame的loc方法选择指定的列，并转换为字典列表
    dict_list = df.loc[:, columns].to_dict(orient='records')
    
    return dict_list
