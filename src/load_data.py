import os

from preprocess import preprocess

def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data'))

    directories = os.listdir(file_path)
    for directory in directories:
        if directory == '.DS_Store':
            continue
        is_spam = True
        if 'nospam' in directory:
            is_spam = False
        
        raw_training_set = [] 
        dir_path = os.path.join(file_path, directory) 
        for file_name in os.listdir(dir_path):
            if file_name == '.DS_Store':
                continue
            file = open(os.path.join(dir_path, file_name))
            processed_email = preprocess(file_name, file.read())
            raw_training_set.append({
                'contents': processed_email,
                'is_spam': is_spam,
            })
    return raw_training_set
