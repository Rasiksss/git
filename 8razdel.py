import pandas as pd
import numpy as np
from scipy import stats
import math
import matplotlib.pyplot as plt
import pingouin as pg

data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataX = data.parse(1)
A5 = dataX['A5']
A6 = dataX['A6']
cpearson = stats.pearsonr(A5, A6)
cspearman = stats.spearmanr(A5, A6)
ckendall = stats.kendalltau(A5, A6)
n = len(A5)
kovt = np.cov(A5, A6, ddof=1)[0, 1]
varA5 = np.std(A5, ddof=1)
varA6 = np.std(A6, ddof=1)
evals = kovt / (varA5 * varA6)
low = evals + (evals * (1 - evals ** 2) / (2 * n)) - stats.norm.ppf(1 - 0.1 / 2) * (1 - evals ** 2) / np.sqrt(n)
high = evals + (evals * (1 - evals ** 2) / (2 * n)) + stats.norm.ppf(1 - 0.1 / 2) * (1 - evals ** 2) / np.sqrt(n)
alpha = 0.1
# z = stats.norm.ppf(1 - alpha/2)
# se = np.sqrt((1 - cpearson**2) / (n - 2))
# lower = cpearson - z * se
# upper = cpearson + z * se
# print(eval)
#z_stat = eval * np.sqrt(1071) / np.sqrt(1 - eval ** 2)
# print(z_stat)
# print(stats.t.ppf(1 - 0.1 / 2, df=1071))
# A5 = A5.astype(float)
# A6 = A6.astype(float)
# A5massiv = A5.to_numpy()
# A6massiv = A6.to_numpy()
# A5massiv -= np.mean(A5)
# A6massiv -= np.mean(A6)
# pooled = A5massiv * A6massiv
# kov = sum(pooled) / n
# evalt = kov / (varA5 * varA6)
# print(evalt)
# print(evals)
r, p_value = stats.pearsonr(A5, A6)
t_stat = r * np.sqrt((n - 2) / (1 - r**2))
rho, p_value1 = stats.spearmanr(A5, A6)

# t_stat1 = rho * np.sqrt((n - 2) / (1 - rho**2))
# tau, p_value2 = stats.kendalltau(A5, A6)
# z_stat = tau * np.sqrt(4*(n+10)/(9*n))
# print(p_value, t_stat)
# print(p_value1, t_stat1)
# print(p_value2, z_stat)
print(low)
print(high)