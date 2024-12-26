import pandas as pd
import numpy as np
from scipy import stats
import math
import matplotlib.pyplot as plt

data = pd.ExcelFile(r"C:/Users/Расул/Downloads/data_matstat_K5.xls", engine='xlrd')
dataX = data.parse(1)
dataA4A8 = dataX[['A4', 'A8']]
I = dataA4A8[dataA4A8['A4'] == 'I']
IIA = dataA4A8[dataA4A8['A4'] == 'IIA']
IIB = dataA4A8[dataA4A8['A4'] == 'IIB']
meanI = np.mean(I['A8'])
meanIIA = np.mean(IIA['A8'])
meanIIB = np.mean(IIB['A8'])
varI = np.var(I['A8'], ddof=1)
varIIA = np.var(IIA['A8'], ddof=1)
varIIB = np.var(IIB['A8'], ddof=1)
pooledmean = sum((len(I) * meanI, len(IIA) * meanIIA, len(IIB) * meanIIB)) / 1073
wgvar = sum((len(I) * varI, len(IIA) * varIIA, len(IIB) * varIIB)) / 1073
bgvar = sum((len(I) * (meanI - pooledmean) ** 2, len(IIA) * (meanIIA - pooledmean) ** 2,
             len(IIB) * (meanIIB - pooledmean) ** 2)) / 1073
pooledvar = wgvar + bgvar
nesmeval_wgvar = wgvar * 1073 / 2
nesmeval_bgvar = bgvar * 1073 / 1070
nesmval_pooledvar = pooledvar * 1073 / 1072
ekd = bgvar / pooledvar
eko = np.sqrt(ekd)
bartlett = stats.bartlett(I['A8'], IIA['A8'], IIB['A8'])
harkeberraI = stats.jarque_bera(I['A8'])
harkeberraIIA = stats.jarque_bera(IIA['A8'])
harkeberraIIB = stats.jarque_bera(IIB['A8'])
'''Нихера тут ненормальное блять и дисперсии неравны'''
print(stats.f_oneway(I['A8'], IIA['A8'], IIB['A8']))