
def get_vocab_list(training_set):
    vocab_list = {}
    for example in training_set:
        email = example.get('contents')
        for word in email:
            if word in vocab_list:
                vocab_list[word] += 1
            else:
                vocab_list[word] = 1
    vocab_list = sorted(vocab_list, key=vocab_list.__getitem__, reverse=True)[:10000]
    return vocab_list
