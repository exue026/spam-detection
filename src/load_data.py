import os

def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data'))

    directories = os.listdir(file_path)
    for directory in directories:
        if not directory == '250hardnospam':
            continue
        is_spam = True
        if 'nospam' in directory:
            is_spam = False
        
        raw_training_set = [] 
        dir_path = os.path.join(file_path, directory) 
        for file in os.listdir(dir_path):
            if file == '.DS_Store':
                continue
            file = open(os.path.join(dir_path, file))
            raw_training_set.append({
                'contents': file.read(),
                'is_spam': is_spam,
            })
    return raw_training_set
