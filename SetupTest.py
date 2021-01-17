#!/usr/bin/env python

import os
import shutil

src='downloads'
dest='literature'

artists=[
        'hemmingway',
        'avdol',
        'baka',
        'billy'
        ]

test_dirs=[
        'hemmingway in paradise',
        'the adventures of billy the kid',
        'MY LITTLE SISTER IS AVDOL???',
        'WHAT CAN I bAKA-BUR?![ENG]'
        ]
test_files=[
        'avdol',
        'baka.txt',
        'hoopah.ext'
        ]
duplicate_files=[
        'dupah.mp4'
        ]


shutil.rmtree(src, ignore_errors=True)
shutil.rmtree(dest, ignore_errors=True)

os.mkdir(src)
os.mkdir(dest)

for a in artists:
    p = os.path.join(dest, a)
    os.mkdir(p)

for d in test_dirs:
    p = os.path.join(src, d)
    os.mkdir(p)

for f in test_files:
    p = os.path.join(src, f)
    open(p, 'a').close()

p = os.path.join(dest, 'dup')
os.mkdir(p)
for d in duplicate_files:
    sp = os.path.join(src, d)
    dp = os.path.join(dest, 'dup', d)
    open(sp, 'a').close()
    open(dp, 'a').close()
