# 必要ライブラリのインポート
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import japanize_matplotlib

# 関数の定義
def func(x, a, b):
  y = a * x / (b + x)
  return y

# データセットの設定
n = 11
x = [0.3, 0.5, 0.5, 0.7, 0.7, 1, 1, 2, 2, 4, 4]
y = [0.00151, 0.00194, 0.00166, 0.00196, 0.00206, 0.00196, 0.00201, 0.00362, 0.00367, 0.00387, 0.00417]

# カーブフィット
popt, pcov = curve_fit(func, x, y)

x_curveplot = np.linspace(np.min(x) - 1, np.max(x) + 0.2, 1000)
y_curveplot = func(x_curveplot, *popt)


# グラフ・結果の表示
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, y) # scatter: 散布図
ax1.plot(x_curveplot, y_curveplot, color='red', linestyle='dashed') # plot: 折れ線グラフ
plt.xlim(0, np.max(x) + 0.4)
plt.ylim(0, np.max(y) + 0.0010)

plt.title('Michaelis-Mentenプロット')
plt.xlabel('基質溶液 [S] (mmol/L)')
plt.ylabel('反応速度 v (μmol/min)')

plt.show

print('[Vmax, Km] =', popt)
