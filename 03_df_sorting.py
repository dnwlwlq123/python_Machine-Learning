import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fpath = './dataset'
#
# dict_data = {
#     "c0":np.arange(1,4),
#     "c1":np.arange(4,7),
#     "c2":np.arange(7,10),
#     "c3":np.arange(10,13),
#     "c4":np.arange(13,16)
# }
# df = pd.DataFrame(dict_data, index = ["r0", "r1", "r2"])
# print(df)

fname = "vor_r.xlsx"
file = os.path.join(fpath, fname)
vor = pd.read_excel(file)


# df = pd.DataFrame(vor)
#
# mean_col = vor.loc[:, "hz0.04":].mean(axis = 1)
# vor.insert(3, "mean", mean_col)
# vor.sort_values(by = "mean", ascending = False, inplace=True)
# vor.iloc[:10, :4]
#
# vor_df = vor.iloc[:10, :4]
#
# vor_df.iloc[5:, 2] = "post"
#
# idx1 = vor_df.loc[:, "time"] != "Pre"
#
# idx2 = vor_df.loc[:, "mean"]>0.74
#
# print(vor_df[(idx1) & (idx2) & (vor_df.loc[:, "group"] == 1)])

tips_df = sns.load_dataset('tips')
print(tips_df[["total_bill", "tip"]].corr())
plt.scatter(tips_df["total_bill"], tips_df["tip"])
plt.title("total_bill--tip")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.show()

mpg_df = sns.load_dataset('mpg')
mpg_df.insert(1, "kml", mpg_df['mpg'] * 1.60934 / 3.78541)
print(mpg_df)










