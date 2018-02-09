import os
import glob

def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data', '250hardnospam'))

    raw_training_set = [] 

    for file in os.listdir(file_path):
        if file == '.DS_Store':
            continue
        file = open(os.path.join(file_path, file))
        raw_training_set.append({
            'contents': file.read(),
            'is_spam': True,
        })

    return raw_training_set