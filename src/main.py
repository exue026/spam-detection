from load_data import load_data
from vocab_list import get_vocab_list
from feature_extraction import extract_feature_matrix

import vocab_list

def main():
    training_set = load_data()
    vocab_list = get_vocab_list(training_set)
    X = extract_feature_matrix(vocab_list, training_set)
    print(X)

if __name__ == '__main__': main()