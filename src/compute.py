import numpy as np

'''
Given a real number,
maps it to a value between 0 and 1
'''
def sigmoid(z):
    return (1 / (1 + np.exp(-z)))

'''
Given a dataset, our hypothesis, and "expected" values,
returns the cost (or error) of the hypothesis
'''
def cost(h, X, y):
    return 0
'''
Initializes a vector of parameters to be used in our hypothesis
Parameters are initially in the range of [-10, 10)
'''
def init_params(size):
    return np.random.uniform(low=-10, high=10, size=size)

'''
Our hypothesis (or model)
Given a feature vector, outputs a real number
'''
def h(x, theta):
    return np.transpose(theta).dot(x)