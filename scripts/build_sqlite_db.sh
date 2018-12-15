#!/bin/bash

#get this script's path

sqlite3 junctions.sqlite < ./sql/snaptron_schema.sql

mkfifo ./import
cat junctions.bgz | zcat > ./import  &
sqlite3 junctions.sqlite -cmd '.separator "\t"' ".import ./import intron"

sqlite3 junctions.sqlite < ./sql/snaptron_schema_index.sql
rm ./import
