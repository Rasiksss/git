import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataA = data.parse(1)
A13 = dataA['A13']
A15 = dataA['A15']

A15 = sm.add_constant(A15)
model = sm.OLS(A13, A15)
results = model.fit()
f_A13 = results.predict(A15)
#my = np.mean(A13)
#residual_variance = np.mean((A13 - f_A13)**2)
#explained_variance = np.mean((f_A13 - my)**2)
#total_variance = residual_variance + explained_variance
# print(residual_variance)
# print(explained_variance)
# print(total_variance)
# print(np.var(A13, ddof=1))
# a = pd.Series(dataA['A13'], name='Рил значения').reset_index()
# b = pd.Series(f_A13, name='Предсказанные значения').reset_index()
# print(pd.merge(a, b, on='index'))
# print(explained_variance / total_variance)
# print(np.sqrt(explained_variance / total_variance))

# robust_cov = results.get_robustcov_results(cov_type='HC0')
# conf_int = robust_cov.conf_int(alpha=0.05)
# print(robust_cov.conf_int(alpha=0.05))
# print(robust_cov.conf_int(alpha=0.01))
# print(robust_cov.conf_int(alpha=0.1))


'''Это короче график остатков, какой-то он хуевый, впринципе как и диаграмма рассеяния
так что почекай данный. Update:сами данные херовые прост'''
#residuals = A13 - results.fittedvalues
#plt.subplot(1, 1, 1)
#plt.scatter(A15.iloc[:, 1], residuals, color='blue')
#plt.xlabel('A15')
#plt.ylabel('Остатки')
#plt.title('График остатков')
#plt.grid()
#plt.tight_layout()
#plt.show()
# f_statistic = results.fvalue
# p_value = results.f_pvalue
# print(f_statistic, p_value)

conf_int = results.get_prediction(A15).conf_int(alpha=0.1)
plt.figure(figsize=(10, 6))
plt.scatter(A15.iloc[:, 1], A13, label='Данные')
plt.plot(A15.iloc[:, 1], f_A13, color='r', label='Линия регрессии')
plt.plot(A15.iloc[:, 1], conf_int[:, 0], color='g', linestyle='--', label='Нижний ДИ')
plt.plot(A15.iloc[:, 1], conf_int[:, 1], color='g', linestyle='--', label='Верхний ДИ')
plt.xlabel('A15')
plt.ylabel('A13')
plt.title('Разброс точек с линией регрессии и доверительными интервалами')
plt.legend()
plt.grid()
plt.show()