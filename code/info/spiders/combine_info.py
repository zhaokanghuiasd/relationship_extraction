# # # -*- coding: utf-8 -*-
#
# import pandas as pd
# import numpy as np
# import math
#
# feature_info = pd.read_csv(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\info\info\spiders\feature.csv", encoding='utf-8')
# data_info = pd.read_csv(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\info\info\spiders\data.csv", encoding='utf-8')
#
# for index, row in feature_info.iterrows():
#     print(index)
#     if str(row["url"]) == "nan":
#         feature_info.drop(axis=0, index=index, inplace=True)
#
# for index, row in data_info.iterrows():
#     print(index)
#     if str(row["name"]) == "nan":
#         data_info.drop(axis=0, index=index, inplace=True)
#
# feature_list = []
# for data_index, data_row in data_info.iterrows():
#     FLAG = 0
#     for feature_index, feature_row in feature_info.iterrows():
#         print(data_index, feature_index)
#         if data_row["detail_info_link"] == feature_row["url"]:
#             feature_list.append(feature_row["features"])
#             FLAG = 1
#             break
#     if FLAG == 0:
#         feature_list.append("")
#
# data_info.loc[:, 'features'] = feature_list
#
# for index, row in data_info.iterrows():
#     print(index)
#     if str(row["features"]) == "nan" or row["features"] == "":
#         data_info.drop(axis=0, index=index, inplace=True)
#
# data_info.to_csv(r"C:\Users\zhaokanghui\Desktop\bdt上学期资料\independent project\info\info\spiders\all_info.csv", encoding='utf-8', index=False)