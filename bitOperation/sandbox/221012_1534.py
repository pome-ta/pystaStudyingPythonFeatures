# ヒストグラム
import math
import matplotlib.pyplot as plt

m = [math.sin((i / 10) * math.pi) for i in range(200)]

plt.plot(m)

if __name__ == '__main__':
  plt.show()
