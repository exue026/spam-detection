import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.abspath(os.path.join(dir_path, '..', 'raw_data', '500spam', '4.txt'))
    file = open(file_path)
    print(file.read())
    file.close()

if __name__ == "__main__": main()



