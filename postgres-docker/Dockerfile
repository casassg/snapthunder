FROM postgres:alpine
ENV TSV_URL https://storage.googleapis.com/snapthunder/chr1.tsv
ADD schema.sql /
ADD index.sql /
ADD prepare.sh /docker-entrypoint-initdb.d/
RUN rm /docker-entrypoint.sh
COPY docker-entrypoint.sh /usr/local/bin/

RUN ln -s usr/local/bin/docker-entrypoint.sh /
