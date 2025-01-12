import os
import shutil

source_folder = 'read.txt'
destination_folder = 'New/'

if os.path.exists(source_folder):
    shutil.move(source_folder,destination_folder)
else:
    print('file is not exists')