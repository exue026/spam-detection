from load_data import load_data
from vocab_list import get_vocab_list
from feature_extraction import extract_feature_matrix
from compute import init_params
from train import gradient_descent

import plot_data
import vocab_list

import time
import numpy as np

'''
Conventions:

m = # of training examples
n = # of features
theta0 is used for the bias term
x0 is the bias term and always has a value of 1
'''
def main():
    training_set = load_data()

    vocab_list = get_vocab_list(training_set)

    # X is an {m X n + 1} dimensional matrix
    X, y = extract_feature_matrix(vocab_list, training_set)

    # lambda, or the regularization constant
    reg_const = 1

    # parameters of the hypothesis
    theta = init_params(X.shape[1])

    # for declaring convergence
    epsilon = 10 ** -3

    # for determining how big each "step" of gradient descent is
    alpha = 0.06

    start = time.time()

    (theta,
    error,
    error_history, 
    iterations) = gradient_descent(X, y, theta, reg_const, alpha, epsilon)

    end = time.time()

    print('final cost is {}'.format(error))
    print('gradient descent time is {}s'.format(int(end - start)))

    x_label = 'iterations'
    y_label = 'Cost (J)'
    title = 'Cost of hypothesis versus iterations of gradient descent'
    plot_data.plot(iterations, error_history, x_label, y_label, title) 

if __name__ == '__main__': main()