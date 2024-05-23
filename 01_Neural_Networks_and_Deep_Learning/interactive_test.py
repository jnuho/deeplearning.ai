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

def init_parameters_deep(layer_dims):
    """
    layer_dims is a list of dimension for each layer
    l = 1,...,L
    """
    L = len(layer_dims)

    parameters = {}
    for l in range(1,L):
        parameters["W" +str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1])
        parameters["b" +str(l)] = np.zeros((layer_dims[l], 1))
    
    return parameters

def linear_forward(A, W, b):
    Z = np.dot(W,A) + b
    cache = (A, W, b)

    return Z, cache

# vector wise
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def linear_activation_forward(A_prev, W, b, activation):
    
    Z, cache = linear_forward(A_prev, W, b)
    if activation == "relu":

    elif activation == "sigmoid"



if __name__=="__main__":
    layer_dims = [5,3,1]
    # Wi, bi for i=1,...,L-1
    parameters = init_parameters_deep(layer_dims)
    # linear forwad
    # z = wx +b
    # linear activation forward
    # a = sigma(z)

    print(parameters)
