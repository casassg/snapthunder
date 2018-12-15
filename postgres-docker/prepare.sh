#!/bin/bash
set -e
psql --username "$POSTGRES_USER" < /schema.sql
psql -c "\copy intron FROM '/chr1.tsv' WITH (FORMAT CSV,  DELIMITER E'\t');"
psql --username "$POSTGRES_USER" < /index.sql