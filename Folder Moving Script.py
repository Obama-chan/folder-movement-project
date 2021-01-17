#!/usr/bin/env python

import os
import sys
import shutil

#source and destination are arguments
source_dir = sys.argv[1]
dest_dir = sys.argv[2]

print(source_dir)
print(dest_dir)

creator_folders = os.listdir(dest_dir)
for creator in creator_folders:
    for video in os.listdir(source_dir):
        if creator.lower() in video.lower():
            print('check')
            src = os.path.join(source_dir, video)
            print(src + '\n')
            dest = os.path.join(dest_dir, creator)
            print(dest + '\n')
            #if statement to check if duplicate exists
            if os.path.exists(source_dir + '/' + video) and os.path.exists(dest_dir + '/' + creator + '/' + video):
                shutil.rmtree(source_dir + '/' + video) #Removes duplicate folder
                print(video + ' deleted due to being a duplicate\n')
            else:
                shutil.move(src, dest)
                print(video + ' has been successfully moved\n')
