import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# fpath = "./dataset"
# fname = "cars.csv"
# file = os.path.join(fpath, fname)
# cars_df = pd.read_csv(file)
# print(cars_df.head(10))
#
# fname02 = ("mtcars.xlsx")
# file02 = os.path.join(fpath, fname02)
# mtcars_df = pd.read_excel(file02)
# print(mtcars_df.head())
#
# print(type(mtcars_df))
# print(mtcars_df.head())
# print(mtcars_df.tail())
# print(mtcars_df.info())
# print("index = ", mtcars_df.index)
# print("shape = ", mtcars_df.shape)
# print("dtypes = ", mtcars_df.dtypes)
# print("columns = ", mtcars_df.columns)
# print(mtcars_df.describe())
# mtcars_df["cyl"] = mtcars_df["cyl"].astype("category")
# mtcars_df["am"] = mtcars_df["am"].astype("category")
# mtcars_df["vs"] = mtcars_df["vs"].astype("category")
# print(mtcars_df.describe())

# data = {
#     "name":["길동", "꺽정", "이순신"],
#     "algol":["A", "A+", "B"],
#     "basic":["C", "B", "B+"],
#     "python":["B+", "C", "C+"]
# }
# mydf = pd.DataFrame(data)
# print(mydf)
#
# school_list = [[15, "남", "덕영중"],
#                [17, "여", "땡중"]]
# scdf = pd.DataFrame(school_list, columns = ["나이", "성별", "학교"])
# print(scdf)
# print(scdf.index)
# print(scdf.columns)
#


# exam = { "수학":[90,80,70],
#          "영어":[98,89,95],
#          "성별":["남","남","여"],
#          "합격":["True","False","True"]
# }
# exam_df = pd.DataFrame(exam)
# print(exam_df)
# print("shape = ", exam_df.shape)
# print("columns = ",exam_df.columns)
# print("ndim = ", exam_df.ndim)
# print("dtpyes = \n", exam_df.dtypes)

# ##요약통계량(summary statistic)
## head 위에 5개, shape데이터 사이즈, info요약정보량, columns 변수명
# print(sns.get_dataset_names())
# mpg_df = sns.load_dataset("mpg")
# print(mpg_df["mpg"].mean().round(3))
# print(mpg_df["mpg"].median())
# print(mpg_df["mpg"].var().round(3))
# print(mpg_df["mpg"].std().round(3))
# print(mpg_df["mpg"].sem().round(3))
# print(mpg_df["mpg"].min())
# print(mpg_df["mpg"].max())
#
# ##이산형
# print(mpg_df["cylinders"].value_counts())
# print(mpg_df["origin"].value_counts())
# print(mpg_df[["mpg", "weight"]].mean(axis = 0).round(3))
# print(mpg_df[["mpg", "weight"]].var(axis = 0).round(3))
# print("="*50)
# print(mpg_df[["mpg", "weight"]].quantile(0.25))
#
# print("correlation coefficient = \n")
# print(mpg_df[["mpg", "weight"]].corr())
#
# print("상관계수 = \n")
# print(mpg_df[["mpg", "weight"]].corr())
# plt.scatter(mpg_df["weight"], mpg_df["mpg"])
# plt.title("Weight vs MPG")
# plt.xlabel("Weight (kg)")
# plt.ylabel("MPG (mile/gallon)")
# plt.show()

titanic_df= sns.load_dataset('titanic')
print(titanic_df.head())
print("="*50)
print("survived = \n", titanic_df["survived"].value_counts())
print("="*50)
print("mean = \n", titanic_df[["age", "fare"]].mean(axis = 0))
print("="*50)
print("std = \n", titanic_df[["age", "fare"]].std())
print("="*50)
print("min = \n", titanic_df[["age", "fare"]].min())
print("="*50)
print("max = \n", titanic_df[["age", "fare"]].max())




