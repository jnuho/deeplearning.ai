# Package imports
# %%
import numpy as np
import matplotlib.pyplot as plt
from testCases_v2 import *
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets

from datetime import datetime
# %matplotlib inline

np.random.seed(1) # set a seed so that the results are consistent


# %%
# X, Y = load_planar_dataset()
# Visualize the data:
# plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral);

n_x = 100
X1 = np.random.randn(5,3)
print(X1)

mean=0
std_dev= 1
X2 = np.random.normal(mean, std_dev, size=(5, 3))
print(X2)

