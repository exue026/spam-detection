import numpy as np

def extract_feature_matrix(vocab_list, training_set):
    vocab_to_index = get_vocab_to_index(vocab_list) 
    indicies = [words_to_indices(email_obj, vocab_to_index) for email_obj in training_set]
    feature_matrix = get_feature_matrix(indicies, vocab_list) 
    y = np.array([[1 if obj.get('is_spam') else 0 for obj in training_set]]).reshape(len(training_set), 1)
    return (feature_matrix, y)

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

'''
Create an {m x n + 1} matrix where each row is the feature vector of a training example,
there are m training examples, and each column is a specific feature
'''
def get_feature_matrix(indicies, vocab_list):
    feature_matrix = np.zeros((len(indicies), len(vocab_list)), dtype=int)
    for i in range(len(indicies)):
        word_indicies = indicies[i].get('contents')
        for j in range(len(word_indicies)):
            feature_matrix[i,word_indicies[j]] = 1
    bias_terms = np.ones((feature_matrix.shape[0], 1), dtype=int)
    return np.concatenate((bias_terms, feature_matrix), axis=1)