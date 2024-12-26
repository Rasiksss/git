import pandas as pd
import numpy as np
from scipy.stats import rankdata, chi2
import math
import matplotlib.pyplot as plt
import pingouin as pg
from itertools import combinations_with_replacement
data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataX = data.parse(1)
A5 = dataX['A5']
A6 = dataX['A6']
A8 = dataX['A8']
sps = dataX[['A5', 'A6', 'A8']].to_numpy()
print(A5.info())

# def kendall_w(data):
#     n = data.shape[0]
#     k = data.shape[1]
#
#     ranks = np.array([rankdata(row) for row in data])
#
#     S = np.sum(np.var(ranks, axis=0))
#
#     W = (12 * S) / (n**2 * (k**3 - k))
#     return W
#
# chi2_stat = 1073 * 2 * kendall_w(sps)
# p_value = chi2.cdf(chi2_stat, df=1072)
# print(chi2_stat, p_value)
print('hello world')