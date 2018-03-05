from load_data import load_data
from vocab_list import get_vocab_list
from feature_extraction import extract_feature_matrix
from compute import init_params
from train import gradient_descent

import plot_data
import vocab_list
import predict

import time
import numpy as np
import os

TRAIN_MODAL = False

'''
Conventions:

m = # of training examples
n = # of features
theta0 is used for the bias term
x0 is the bias term and always has a value of 1
'''
def main():
    if TRAIN_MODAL:
        train()
    else:
        predict_email()

def predict_email():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path_theta = os.path.abspath(os.path.join(dir_path, '..', 'results', 'params.txt'))
    file_path_vocab = os.path.abspath(os.path.join(dir_path, '..', 'results', 'vocab_list.txt')) 
    theta = np.loadtxt(file_path_theta)
    theta = theta.reshape(theta.shape[0], 1)
    vocab_list = np.loadtxt(file_path_vocab, dtype=str)
    file_path_email = os.path.abspath(os.path.join(dir_path, '..', 'test-email.txt')) 
    email = open(file_path_email, encoding = 'ISO-8859-1')
    is_spam = predict.is_spam(theta, vocab_list, email.read())
    print('email is spam? {}'.format(is_spam))

def train():
    start = time.time()

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

    (theta,
    error,
    error_history, 
    iterations) = gradient_descent(X, y, theta, reg_const, alpha, epsilon)

    np.savetxt('/results/params.txt', theta)
    np.savetxt('/results/vocab_list.txt', vocab_list, fmt='%s')

    end = time.time()

    print('final cost is {}'.format(error))
    print('gradient descent time is {}s'.format(int(end - start)))

    x_label = 'iterations'
    y_label = 'Cost (J)'
    title = 'Cost of hypothesis versus iterations of gradient descent'
    plot_data.plot(iterations, error_history, x_label, y_label, title)
    
    
if __name__ == '__main__': main()