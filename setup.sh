#!/usr/bin/env fish

set SRC downloads
set DEST literature
set ARTISTS "hemmingway" "avdol" "baka" "billy"
set TESTS "hemmingway in paradise" "the adventures of billy the kid" "MY LITTLE SISTER IS AVDOL???" "WHAT CAN I bAKA-BUR?![ENG]"

rm -rf $SRC
rm -rf $DEST

mkdir $DEST
for a in $ARTISTS
  mkdir -p $DEST/$a
end
for t in $TESTS
  mkdir -p $SRC/$t
end
