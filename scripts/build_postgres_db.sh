#!/bin/bash

#get this script's path

psql < ./sql/snaptron_schema_postgres.sql

mkfifo ./import
cat junctions.bgz | zcat > ./import  &
psql -c "\copy intron FROM './import' WITH (FORMAT CSV,  DELIMITER E'\t');"

psql < ./sql/snaptron_schema_postgres_index.sql
rm ./import
