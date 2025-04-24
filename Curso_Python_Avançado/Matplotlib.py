import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(7)

y = np.random.randint(low=1, high=1500, size=10)

print(y)


print(plt.plot(y))
plt.show()


