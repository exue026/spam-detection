import os
import glob

def load_data():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data', '250hardnospam'))

    file = open(os.path.join(file_path, os.listdir(file_path)[40]))
    print(file.read())
