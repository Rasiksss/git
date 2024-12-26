import pandas as pd
import numpy as np
from scipy.stats import chi2
import math
import matplotlib.pyplot as plt

data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataX = data.parse(1)
X9 = dataX['A9']
X14 = dataX['A14']
contiguencytable = pd.crosstab(X9, X14)
stacked = contiguencytable.stack()
formatted_table = contiguencytable.copy().astype('float64')

for (row, col), value in stacked.items():
    expected_value = (np.sum(contiguencytable.loc[:, col]) * np.sum(contiguencytable.loc[row, :]) / 1073)
    formatted_table.loc[row, col] = round(expected_value, 2)

z_stat = 0

for (row, col), value in stacked.items():
    z_stat += ((contiguencytable.loc[row, col] - formatted_table.loc[row, col]) ** 2) / formatted_table.loc[row, col]
print(1-chi2.cdf(z_stat, df=4))

