import os
import sys

directory = sys.argv[1]
print('Make folders in this directory' + directory)
name = ' '

while name != 'stop':
    name = input('Foldername?:')
    path = os.path.join(directory,name)
    os.mkdir(path)
    print('Created' + name , ' directory')
