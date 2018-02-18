from load_data import load_data
from vocab_list import get_vocab_list
from feature_extraction import extract_feature_matrix

import vocab_list

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
    X = extract_feature_matrix(vocab_list, training_set)
    print(X.shape[1])

if __name__ == '__main__': main()