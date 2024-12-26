import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import t
# Загрузка данных
data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataA = data.parse(1)
Y = dataA['A13']
X = dataA['A15']

X_squared = X ** 2
X_matrix = pd.DataFrame({'X': X, 'X_squared': X_squared})

X_matrix = sm.add_constant(X_matrix)
model = sm.OLS(Y, X_matrix).fit()
coefficients = model.params
# print(coefficients)
# print(model.summary())
f_A13 = model.predict(X_matrix)
my = np.mean(Y)
residual_variance = np.mean((Y - f_A13)**2)
explained_variance = np.mean((f_A13 - my)**2)
total_variance = residual_variance + explained_variance
norm_total_var = np.var(Y, ddof=1)
# print(residual_variance)
# print(explained_variance)
# print(total_variance)
# print(norm_total_var)
# print(explained_variance / total_variance)
# print(np.sqrt(explained_variance / total_variance))
# nesm_residual = 1073 * residual_variance / 1070
# nesm_explained = 1073 * explained_variance / 2
# nesm_total = 1073 * norm_total_var / 1072
# print(nesm_explained, explained_variance)
# print(nesm_residual, residual_variance)
# print(nesm_total, norm_total_var)
X = X.to_numpy()
Y = Y.to_numpy()
F = np.array([np.array([1] * 1073), X, X**2])
F_FT = np.dot(F, F.transpose())

def f(x):
    return 460.11824200766114 + 1.0224467763908305 * x - 0.0009 * (x ** 2)


X1 = np.sort(X)
D_res_new = np.sum((f(X) - Y) ** 2) / (1073 - 3)
quantile = t(1073 - 3).ppf(1- 0.1/2)
x_arr = np.array([1, X1, X1 ** 2], dtype='object')
flow = f(X1) - quantile * np.sqrt(D_res_new * x_arr.transpose() @ np.linalg.inv(F_FT) @ x_arr)
fhigh = f(X1) + quantile * np.sqrt(D_res_new * x_arr.transpose() @ np.linalg.inv(F_FT) @ x_arr)

# plt.scatter(X, Y, color='red')
# plt.plot(X1, f(X1), color='lime', linewidth=0.8)
# plt.plot(X1, fhigh, linestyle='-', color='red', linewidth=0.8)
# plt.plot(X1, flow, linestyle='-', color='red', linewidth=0.8)
# plt.grid()
# plt.show()

#residual = Y - f(X)
#plt.scatter(X, residual, color='red')
#plt.xlabel('Значения  X')
#plt.ylabel('остатки')
#plt.grid()
#plt.show()
f_stat = model.fvalue
p_value = model.f_pvalue
print(f_stat, p_value)