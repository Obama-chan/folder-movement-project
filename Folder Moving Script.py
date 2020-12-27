#!/usr/bin/env python

import os
import sys
import shutil

src_dir = sys.argv[1]
dest_dir = sys.argv[2]

print(src_dir)
print(dest_dir)

artists = os.listdir(dest_dir)

for artist in artists:
	for folder in os.listdir(src_dir):
		if artist.lower() in folder.lower():
			src = os.path.join(src_dir, folder)
			dest = os.path.join(dest_dir, artist)
			shutil.move(src, dest)
			print (folder + ' succesfully moved')
