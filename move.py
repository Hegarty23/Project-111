import os
import shutil

from_dir = "C:/Users/david_mnqnbf1/Downloads"
to_dir = "C:/Users/david_mnqnbf1/Desktop"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
     root, extension = os.path.splitext(filename)
print(root)
print(extension)