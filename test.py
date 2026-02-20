import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Numpy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)

# Small plot test
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Day 1 Test Plot")
plt.show()
