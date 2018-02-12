import os
import re
import sys
import nltk
import numpy as np

def setupNltk():
    sys.path.append("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")
    nltk.download('punkt')

def regex_expr(expr, replace, string):
    return re.sub(re.compile(expr), replace, string)

def preprocess(file_name, email):
    try:
        header_end = email.index('\n\n')
    except ValueError:
        print(file_name)
        print(email)
        assert(False)

    email = email[header_end:]
    email = email.lower()
    email = regex_expr('<[^<>]+>', ' ', email)
    email = regex_expr('[0-9]+', 'number', email)
    email = regex_expr('(http|https)://[^\s]*', 'httpaddr', email)
    email = regex_expr( '[^\s]+@[^\s]+', 'emailaddr', email)
    email = regex_expr('[$]+', 'dollar', email)
    email = regex_expr('[^a-zA-Z0-9]', ' ', email)
    email = ' '.join(email.split())
    tokens = nltk.tokenize.word_tokenize(email)
    stemmer = nltk.stem.PorterStemmer()
    email = [stemmer.stem(word) for word in tokens]

    return np.array(email)
