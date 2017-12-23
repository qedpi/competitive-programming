import numpy as np
import matplotlib.pyplot as plt


s = "topcodertpcder"
s2 = "cbbaca"
xs = [ord(c) for c in s2]

plt.plot(xs)
plt.ylabel("char values")
plt.xlabel("chars")
plt.show()