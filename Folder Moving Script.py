#!/usr/bin/env python

import os
import sys
import shutil

#source and destination are arguments
source_dir = sys.argv[1]
dest_dir = sys.argv[2]

print(source_dir)
print(dest_dir)
print()

creator_folders = os.listdir(dest_dir)
for creator in creator_folders:
    for filename in os.listdir(source_dir):
        if creator.lower() in filename.lower():

            src = os.path.join(source_dir, filename)
            dest = os.path.join(dest_dir, creator)

            print(src)
            print(dest)

            if os.path.exists(os.path.join(dest, filename)):
                # need to delete a duplicate
                if os.path.isdir(src):
                    # dealing with a torrent directory
                    shutil.rmtree(src)
                else:
                    # dealing with a regular file
                    os.remove(src)

                print(filename + ' deleted due to being a duplicate\n')
            else:
                # just move it
                shutil.move(src, dest)
                print(filename + ' has been successfully moved\n')
