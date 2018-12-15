#!/bin/bash

#get this script's path

psql < ./sql/snaptron_schema_postgres.sql

mkfifo ./import
cat junctions.bgz | zcat | grep 'chr1\t' > ./import  &
psql -c "\copy intron_chr1 FROM './import' WITH (FORMAT CSV,  DELIMITER E'\t');"

psql < ./sql/snaptron_schema_postgres_index.sql
rm ./import
