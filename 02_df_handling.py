import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fpath = "./dataset"

# exam_data = {
#     "수학":[90, 80, 90],
#     "영어":[98, 89, 95],
#     "성별":["남", "남","여"],
#     "합격":[True, False, True]
# }
#
# exam_df = pd.DataFrame(exam_data)
#
# list_df = [["green", "M", 13.5, "class1"],
#            ["red", "L", 15.3, "class2"],
#            ["blue", "XL", 10.1, "class1"]]
# df = pd.DataFrame(list_df, columns=["color", "size", "price", "classlabel"])
# print(df)
# #변수명 바꾸기
# df.rename(columns = {"color" : "색깔",
#                      "size" : "크기",
#                      "price": "가격",
#                      "classlabel" : "클래스"},
#                      index = {0:1, 1:2, 2:3},
#                      inplace = True)
# print(df)
# ##########
# print('exam_df = \n', exam_df)
# exam_df_wo_math = exam_df.drop(labels = ["수학"], axis = 1, inplace = True)
# print(exam_df)
# exam_df.drop(labels = ["영어", "합격"], axis = 1, inplace = True)
# print(exam_df)
# exam_df.drop(labels = [0], axis = 0, inplace=True)
# print(exam_df)

# fpath = "./dataset"
# fname = "vor_r.xlsx"
# file = os.path.join(fpath, fname)
# vor = pd.read_excel(file)
# print(vor.head(10))
#
# vor.rename(columns = {"group" : "소속",
#                       "id" : "번호"},
#                        inplace = True)
# print(vor)
# vor.drop(labels = ["소속", "번호"], axis = 1, inplace=True)
# print(vor)
# exam_data = {
#     "수학":[90, 80, 90],
#     "영어":[98, 89, 95],
#     "성별":["남", "남","여"],
#     "합격":[True, False, True]
# }
#
# exam_df = pd.DataFrame(exam_data)
# ##꼭 데이터는 살리고 값은 None으로 포현하고싶을때
# # exam_df.loc[0, "성별"] = np.nan
# # exam_df.loc[1, "수학" : "영어"] = None
# # print("*"*50)
# # print(exam_df)
# # print("*"*50)
# # print(exam_df.dropna(axis = 0)) # row 방향 삭제
# # print(exam_df.dropna(axis = 1)) # column 방향 삭제
# print("수학")
# print(exam_df["수학"])
# print(exam_df[["성별", "수학"]])
# print(exam_df)
# print(exam_df.loc[1:2, ["수학", "영어"]])
# print(exam_df.loc[1:2, "수학": "영어"])


# df = pd.DataFrame({
#     'hdz':['yes', 'no', 'no', 'no', 'yes'],
#     'chestpain': [True, False, False, True, False],
#     'cholesterol':[208, 282, 235, 277, 280],
#     'sysbp': [160, 140, 188, 162, 122]
# }, index = np.arange(5))

# print(df.loc[[2,4], "chestpain"])
# print("*"*50)
# print(df.loc[1:3, ["chestpain", "cholesterol", "sysbp"]])
# print("*"*50)
# print(df.loc[:, "hdz"])
# print("*"*50)
# print(df.loc[:, ::-1])

# exam_data = {
#     "수학":[90, 80, 90],
#     "영어":[98, 89, 95],
#     "성별":["남", "남","여"],
#     "합격":[True, False, True]
# }
# exam_df = pd.DataFrame(exam_data)
# exam_df["음악"] = [100, 90, 50]
# exam_df.insert(1, "코딩", [50,80,100]) # columns
# exam_df.loc[3] = [80, 30, 40, "여", True, 29]
# exam_df.loc[3, "코딩"] = 0
# exam_df.loc[2, "코딩":"영어"] = 0
# print(exam_df)

# df = pd.DataFrame({
#     'hdz':['yes', 'no', 'no', 'no', 'yes'],
#     'chestpain': [True, False, False, True, False],
#     'cholesterol':[208, 282, 235, 277, 280],
#     'sysbp': [160, 140, 188, 162, 122]
# }, index = np.arange(5))
#
# df.loc[4, "sysbp"] = 10000
# df.loc[1:3, ["sysbp"]] = 1,2,3
# print(df)

# dict_data = {
#     "c0":np.arange(1,4),
#     "c1":np.arange(4,7),
#     "c2":np.arange(7,10),
#     "c3":np.arange(10,13),
#     "c4":np.arange(13,16)
# }
# df = pd.DataFrame(dict_data, index = ["r0", "r1", "r2"])
# print(df)
# print("*"*50)
# df.set_index("c0", inplace=True)
# df.reset_index(inplace=True)
# print(df)

fname = "vor_r.xlsx"
file = os.path.join(fpath, fname)
vor = pd.read_excel(file)
print(vor.head(5))

vor.set_index("id", inplace=True)
print(vor.head(5))

