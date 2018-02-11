from load_data import load_data
from vocab_list import get_vocab_list

import vocab_list

def main():
    training_set = load_data()
    vocab_list = get_vocab_list(training_set)
    print(vocab_list)

if __name__ == '__main__': main()