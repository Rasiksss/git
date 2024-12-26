import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns

X = np.random.uniform(-5, 5, 300)
Y = np.random.uniform(-5, 5, 300)
U = np.array([])

def corr_pir():
    n = 300
    H = []
    KKP = []
    RKS = []
    RKK = []
    while n:
        h = np.random.uniform(0, 1)
        H.append(h)
        U = h * (X ** 3) + (1 - h) * (Y ** 3)
        pearson = stats.pearsonr(X, U)[0]
        spearman = stats.spearmanr(X, U)[0]
        kendall = stats.kendalltau(X, U)[0]
        KKP.append(pearson)
        RKS.append(spearman)
        RKK.append(kendall)
        n -= 1
    return H, KKP, RKS, RKK


fig, axes = plt.subplots(1, 3, figsize=(10, 5))
axes.flatten()
H, KKP, RKS, RKK = corr_pir()
koff = [KKP, RKS, RKK]
koff_name = ['KKP', 'RKS', 'RKK']
font_size_title = 8
font_size_labels = 9
for i in range(len(axes)):
    sns.regplot(x=H, y=koff[i], ax=axes[i], scatter_kws={'alpha': 0.7, 's': 3}, line_kws={'color': 'red'})
    axes[i].set_title(f'График разброса для {koff_name[i]} с линией регрессии', fontsize=font_size_title)
    axes[i].set_xlabel('Лямбда')
    axes[i].set_ylabel(koff_name[i])
    axes[i].set_xlim(-0.5, 1.5)
    axes[i].set_ylim(0, 1.5)
    axes[i].grid(True)

plt.suptitle('Графики разброса с линиями регрессии', fontsize=font_size_title)
plt.tight_layout()
plt.show()