# 必要ライブラリのインポート
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import japanize_matplotlib

# 関数の定義
def func(x, a, b):
  y = b /a * x + 1 / a
  return y

# データセットの設定
n = 11
x_origin = [0.3, 0.5, 0.5, 0.7, 0.7, 1, 1, 2, 2, 4, 4]
y_origin = [0.00151, 0.00194, 0.00166, 0.00196, 0.00206, 0.00196, 0.00201, 0.00362, 0.00367, 0.00387, 0.00417]

x = np.reciprocal(x_origin)
y = np.reciprocal(y_origin)

# カーブフィット
popt, pcov = curve_fit(func, x, y)

x_curveplot = np.linspace(-2.5, 3.5, 1000)
y_curveplot = func(x_curveplot, *popt)


# グラフ・結果の表示
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(x, y) # scatter: 散布図を書く
ax1.plot(x_curveplot, y_curveplot, color='red', linestyle='dashed')
ax1.axvline(x=0, color='black', linewidth=1)
ax1.axhline(y=0, color='black', linewidth=1)

plt.title('Lineweaver-Burkプロット')
plt.xlabel('1/[S]')
plt.ylabel('1/v')

plt.show

print('[Vmax, Km] =', popt)
