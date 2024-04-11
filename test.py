import numpy as np
import h5py
import matplotlib.pyplot as plt
# from testCases_v2 import *
# from dnn_utils_v2 import sigmoid, sigmoid_backward, relu, relu_backward

# %matplotlib inline
plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'
plt.show()

# %load_ext autoreload
# %autoreload 2


np.random.seed(1)


def L_model_forward(X, parameters):
  A = X
  cache = []

  AL = None

  return AL, cache



if __name__=="__main__":
  X = np.random.randn(1,3)
  print(X)

# Turn on interactive mode
plt.ion()

# Create a simple plot
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# A figure with just one sub-plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')

# Show the plot (in interactive mode, this should not be necessary)
plt.show()