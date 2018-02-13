from load_data import load_data
from vocab_list import get_vocab_list
from feature_extraction import get_feature_vector

import vocab_list

def main():
    training_set = load_data()
    vocab_list = get_vocab_list(training_set)
    word_indicies = get_feature_vector(vocab_list, training_set)

if __name__ == '__main__': main()