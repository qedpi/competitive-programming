import numpy as np
import matplotlib.pyplot as plt


s1 = "cbacba"
s2 = "cbbaca"
xs = [ord(c) for c in s1]

plt.plot(xs)
plt.ylabel("ASCII values")
plt.xlabel("chars")
plt.show()