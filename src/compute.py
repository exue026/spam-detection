import numpy as np
import math

'''
Given a real number,
maps it to a value between 0 and 1
'''
def sigmoid(z):
    sig = np.vectorize(lambda x: (1 / (1 + np.exp(-x))))
    return sig(z)

'''
element-wise natural logarithmn function
'''
def Log(vector):
    log = np.vectorize(lambda x: math.log(x)) 
    return log(vector)

'''
Given a dataset, our hypothesis, and "expected" values,
returns the cost (or error) of the hypothesis
'''
def cost(h, X, theta, y):
    m = y.shape[0]
    predictions = H(X, theta)
    return (-1 / m) * np.sum(y * Log(predictions) + (1 - y) * Log(1 - predictions))
    
'''
Initializes a vector of parameters to be used in our hypothesis
Parameters are initially in the range of [-10, 10)
'''
def init_params(size):
    return np.random.uniform(low=-10, high=10, size=size)

'''
Our hypothesis (or model)
Given a feature vector, outputs a real number (prediction)
'''
def h(x, theta):
    return sigmoid(np.transpose(theta).dot(x))

'''
Modified version of hypothesis
Given a {m X n + 1} matrix, return a {m X 1} vector,
each row being prediction for the specific traininge example
'''
def H(X, theta):
    return sigmoid(X.dot(theta))