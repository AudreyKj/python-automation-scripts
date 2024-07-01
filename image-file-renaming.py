import os
import sys
import re

if(len(sys.argv) < 3):
    print('Please provide a folder path and a new name.')
    sys.exit(1)

path = sys.argv[1]
name = sys.argv[2]

folder = os.listdir(path)
count = 1
image_extensions = ('jpeg', 'jpg', 'png', 'tiff', 'gif')
base_path = path + '/'
file_extension_pattern = r'\.[^.]+$'

for file in folder:
    if(file.lower().endswith(image_extensions)):
        match = re.search(file_extension_pattern, file)
        file_extension = match.group(0)
        new_name = f"{name}_{count}"
        old_path = base_path + file
        new_path = f"{base_path}{new_name}{file_extension}"
        os.rename(old_path, new_path)
        count+=1
