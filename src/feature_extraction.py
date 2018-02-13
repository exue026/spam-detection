
def get_feature_vector(vocab_list, training_set):
    vocab_to_index = get_vocab_to_index(vocab_list) 
    training_set = [words_to_indices(email_obj, vocab_to_index) for email_obj in training_set]
    return training_set

def get_vocab_to_index(vocab_list):
    memo = {}
    for i in range(len(vocab_list)):
        memo[vocab_list[i]] = i
    return memo

def words_to_indices(email_obj, vocab_to_index):
    email = email_obj.get('contents')
    indicies = []
    for word in email:
        indicies.append(vocab_to_index.get(word, -1))
    email_obj['contents'] = list(filter(lambda x: x >= 0, indicies))
    return email_obj