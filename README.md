# Snapthunder

Genomic data is being accumulated at an exponential rate. The need to parallelize data analysis and storage is becoming stronger. In this paper, there's a proposal for scaling indexing on RNA splicing data. Distributing the data across several servers will allow for parallelized jobs to run on top of it, leveraging the power of data locality. Moving to a cloud infrastructure allows achieving such distribution while keeping reproducibility high.


Here is an explanation of each folder, its contents and how to run it.

## Analysis

Contains Python scripts to run perfomance queries in different database settings on a local machine. It also includes csvs and Excel sheet with all the data as generated in my personal laptop.

### Run
Requirements: `python3`, `virtualenv`
Data requirements:
- Postgres database with `intron` table containing all GTEx junction data indexed
- Postgres database with `intron_chr1` table containing chromosome 1 GTEx junction data indexed
- SQLite database in project root folder as `junctions.sqlite` with `intron` table containing all GTEx junction data indexed
- SQLite database in project root folder as `junctionschr1.sqlite` with `intron` table containing chromosome 1 GTEx junction data indexed

Commands:
- `virtualenv env --python=python3`
- `source env/bin/activate`
- `pip3 install requirements.txt`
- `python analysis/script.py` (replace scipt with script name) 

## Kubernetes 

Contains Kubernetes object definition for each of the services defined in the paper. 

### Deploy
Requirements: Kubernetes cluster, `kubectl` configured to access the cluster.

- `kubectl create -f kubernetes/chr1ps.yaml`
- `kubectl create -f kubernetes/ui.yaml`

## Postgres Docker

Contains files to create custom postgres container. 

### Development

Requirements: Local Postgres instance

Commands:
- `cd postgres-docker`
- `wget -nc https://storage.googleapis.com/snapthunder/chr1.tsv`
- `./prepare.sh`

### Docker container creation

Requirements: `docker`, hosted `tsv` with chromosome 1 data.

- `make` for building image
- `make push` for pushing image to Docker Hub repository

Note that currently is configured to push to my Docker Hub repository (casassg). Replace with your user or desired repository name.

## Scripts

Contains scripts to populate databases for local testing. 

Requirements: 
- `junctions.bgz` downloaded from snaptron web server: `curl -o junctions.bgz http://snaptron.cs.jhu.edu/data/gtex/junctions.bgz`.
- Running postgres server in local machine.

## UI Docker

Contains code for UI and API server.

### Development

Requirements: `python3`, `virtualenv`
Data requirements:
- Postgres database with `intron` table containing chromosome 1 GTEx junction data indexed

Commands:
- `virtualenv penv --python=python3`
- `source penv/bin/activate`
- `pip3 install requirements.txt`
- `python ui-docker/server.py` 

Requires changes in the server.py code to point to `localhost` instead of the remote name server. It also needs to change username and database according to your local Postgres set up.


### Docker container creation

Requirements: `docker`

- `make` for building image
- `make push` for pushing image to Docker Hub repository

Note that currently is configured to push to my Docker Hub repository (casassg). Replace with your user or desired repository name.

## Attributions 

- Project based upon [Snaptron by  Christopher Wilks](https://github.com/ChristopherWilks/snaptron)
