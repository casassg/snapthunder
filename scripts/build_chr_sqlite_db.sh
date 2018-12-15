#!/bin/bash

#get this script's path

sqlite3 junctionschr1.sqlite < ./sql/snaptron_schema.sql

mkfifo ./import
cat junctions.bgz | zcat | grep 'chr1\t' > ./import  &
sqlite3 junctionschr1.sqlite -cmd '.separator "\t"' ".import ./import intron"

sqlite3 junctionschr1.sqlite < ./sql/snaptron_schema_index.sql
rm ./import