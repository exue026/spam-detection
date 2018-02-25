
#!/usr/bin/env python

import glob, os

i = 0
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for file in files:
        if file.endswith('.DS_Store'):
            path = os.path.join(root, file)

            print("Deleting: {}".format(path))

            if os.remove(path):
                print ("Unable to delete!")
            else:
                print ("Deleted...")
                i += 1

print("Files Deleted: {}".format(i))