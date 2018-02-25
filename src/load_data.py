import os
import numpy as np

from preprocess import preprocess

def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data'))

    directories = os.listdir(file_path)
    raw_training_set = [] 

    for directory in directories:
        if directory == '.DS_Store':
            continue
        print(directory)
        is_spam = True
        if 'nospam' in directory:
            is_spam = False
        
        dir_path = os.path.join(file_path, directory) 
        temp = 0
        for file_name in os.listdir(dir_path):
            if file_name == '.DS_Store':
                continue
            file = open(os.path.join(dir_path, file_name), encoding = 'ISO-8859-1')
            processed_email = preprocess(file_name, file.read())
            raw_training_set.append({
                'contents': processed_email,
                'is_spam': is_spam,
            })

    return np.array(raw_training_set)
