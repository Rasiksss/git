import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import t

data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataA = data.parse(1)
Y = dataA['A13']
X1 = dataA['A15']
X2 = dataA['A5']
X_matrix = pd.DataFrame({'X1': X1, 'X2': X2})
X_matrix = sm.add_constant(X_matrix)
model = sm.OLS(Y, X_matrix).fit()
coefficients = model.params
f_A13 = model.predict(X_matrix)
my = np.mean(Y)
residual_variance = np.mean((Y - f_A13)**2)
explained_variance = np.mean((f_A13 - my)**2)
total_variance = residual_variance + explained_variance
norm_total_var = np.var(Y, ddof=1)
nesm_residual = 1073 * residual_variance / 1070
nesm_explained = 1073 * explained_variance / 2
nesm_total = 1073 * norm_total_var / 1072
Kd = explained_variance / norm_total_var
Ko = np.sqrt(Kd)
print(Kd, Ko)