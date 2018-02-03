import os
import re

def regex_expr(expr, replace, string):
    return re.sub(re.compile(expr), replace, string)

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data', '500spam', '490.txt'))
    file = open(file_path)
    email = file.read()
    header_end = email.index('\n\n')
    email = email[header_end:]
    email = email.lower()
    email = regex_expr('<[^<>]+>', ' ', email)
    email = regex_expr('[0-9]+', 'number', email)
    email = regex_expr('(http|https)://[^\s]*', 'httpaddr', email)
    email = regex_expr( '[^\s]+@[^\s]+', 'emailaddr', email)
    email = regex_expr('[$]+', 'dollar', email)
    email = regex_expr('[^a-zA-Z0-9]', ' ', email)
    email = nltk.word_tokenize(email)
    print(email)
    file.close()

if __name__ == "__main__": main()



