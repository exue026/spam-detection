from preprocess import preprocess
from feature_extraction import extract_feature_vector
from compute import h

def is_spam(theta, vocab_list, email):
   processed_email = preprocess(None, email) 
   feature_vector = extract_feature_vector(vocab_list, processed_email)
   return True if h(feature_vector, theta) >= 0.5 else False


