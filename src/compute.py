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
def cost(h, X, theta, y, reg_const):
    m = y.shape[0]
    predictions = h(X, theta)
    reg_term = (reg_const / (2 * m)) * np.sum(np.square(theta[1:]))
    error = (1 / m) * np.sum(-y * Log(predictions) - (1 - y) * Log(1 - predictions)) + reg_term
    return error
'''
Calculates the gradient of the cost function w.r.t the parameters
Specifically, calculates the rate of change of the cost function with respect to a parameter,
for each parameter of the hypothesis
'''
def gradient(h, X, theta, y, reg_const):
    m = y.shape[0]
    errors = h(X, theta) - y
    # vectorized implementation of calculating the gradient
    # np.transpose(X) is a {n + 1 X m} matrix
    # each row represents all the values of a particular feature across all
    # training examples
    grads = (1 / m) * np.transpose(X).dot(errors) 
    grads[1:] = grads[1:] + (reg_const / m) * theta[1:]
    return grads
    
'''
Initializes a vector of parameters to be used in our hypothesis
Parameters are initially in the range of [-10, 10)
'''
def init_params(size):
    return np.zeros((size, 1))

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
    raw_predictions = X.dot(theta)
    return sigmoid(raw_predictions)