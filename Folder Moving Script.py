#Sorting Files
import os
import sys
import shutil

#Get path info from user
Print ("Option 1: Moving a Directory to another directory.\n" + "Option 2: Moving a file to a directory\n"


#r'C:\Users\Obama-Chan\Desktop\Source'
path = input("Gimme the path to folder you want to move Files from:\n")
print ("Starting path is: " + path)

#destination = r'C:\Users\Obama-Chan\Desktop\Destination'
dest = input("Now give me the path of the folder you want to move the files to:\n")
print ("Destination path is:" + dest) 




folders = os.listdir(path)
for folder in folders:
        folderName = input("Enter Full name of file or keyword in filename:\n")
        if folderName.lower() in folder.lower():
                shutil.move(os.path.join(path, folder), dest)
        print (folder + ' succesfully moved')

