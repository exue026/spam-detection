import os
import re
import sys

def regex_expr(expr, replace, string):
    return re.sub(re.compile(expr), replace, string)

def preprocess():
    sys.path.append("/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")
    from nltk.tokenize import word_tokenize
    from nltk.stem import PorterStemmer
    import nltk
    nltk.download('punkt')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data', '500spam', '490.txt'))
    file = open(file_path)
    email = file.read()
    file.close()
    header_end = email.index('\n\n')
    email = email[header_end:]
    email = email.lower()
    email = regex_expr('<[^<>]+>', ' ', email)
    email = regex_expr('[0-9]+', 'number', email)
    email = regex_expr('(http|https)://[^\s]*', 'httpaddr', email)
    email = regex_expr( '[^\s]+@[^\s]+', 'emailaddr', email)
    email = regex_expr('[$]+', 'dollar', email)
    email = regex_expr('[^a-zA-Z0-9]', ' ', email)
    email = ' '.join(email.split())
    tokens = word_tokenize(email)
    stemmer = PorterStemmer()
    email = [stemmer.stem(word) for word in tokens]
    print(email)

