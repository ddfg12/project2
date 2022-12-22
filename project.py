import os
import shutil
from_dir="C:/Users/User/Desktop/c-101/documents"
to_dir="C:/Users/User/Downloads"
listoffiles=os.listdir(from_dir)
#print(listoffiles)
for file_name in listoffiles:
    name,extension = os.path.splitext (file_name)
    print(name)
    print(extension)
