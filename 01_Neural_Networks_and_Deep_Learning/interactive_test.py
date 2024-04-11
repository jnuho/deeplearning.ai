# Package imports
# %%
import numpy as np
import h5py
import matplotlib.pyplot as plt
from testCases_v2 import *
from dnn_utils_v2 import sigmoid, sigmoid_backward, relu, relu_backward

# %matplotlib inline
plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# %load_ext autoreload
# %autoreload 2

np.random.seed(1)

def relu(Z):
  A = np.maximum(0,Z)
  cache = Z

  return A, cache

def sigmoid(Z):
  A = 1/(1+np.exp(-Z))
  cache = Z

  return A, cache

def linear_forward(A_prev, W,b):
  Z = np.dot(W,A_prev) + b
  cache = (A_prev, W, b)

  return Z, cache

def linear_activation_forward(A_prev, W, b, activation):

  if activation=="relu":
    Z, linear_cache = linear_forward(A_prev, W, b)
    A, activation_cache = relu(Z)
  elif activation=="sigmoid":
    Z, linear_cache = linear_forward(A_prev, W, b)
    A, activation_cache = relu(Z)

  cache = (linear_cache, activation_cache)

  return A, cache

def init_parameters_deep(layer_dims):
  L = len(layer_dims)
  parameters = {}

  # l = 1,2,... L-1
  for l in range(1, L):
    parameters["W"+str(l)]= np.random.randn(layer_dims[l], layer_dims[l-1])*.01
    parameters["b"+str(l)]= np.zeros((layer_dims[l],1))

  return parameters
  
def L_model_forward(X, parameters):
  A = X
  caches = []
  L = len(parameters) // 2
  for l in range(1,L):
    A_prev = A
    A, cache = linear_activation_forward(A_prev,
                                         parameters["W"+str(l)],
                                         parameters["b"+str(l)],
                                         activation="relu"
                                         )
    caches.append(cache)
  
  AL, cache = linear_activation_forward(A,
                                         parameters["W"+str(L)],
                                         parameters["b"+str(L)],
                                         activation="sigmoid")
  caches.append(cache)

  return AL, caches


if __name__=="__main__":
  layer_dims = [5,3,1]
  # Wi, bi for i=1,...,L-1
  parameters = init_parameters_deep(layer_dims)

  print(parameters)