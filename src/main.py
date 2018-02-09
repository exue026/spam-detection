from load_data import load_data
from preprocess import preprocess
import vocab_list

def main():
    raw_training_set = load_data()
    training_set = preprocess(raw_training_set)
    print(training_set[3].get('contents'))

if __name__ == '__main__': main()