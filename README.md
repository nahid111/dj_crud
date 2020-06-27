# django CRUD


## installation
- install pipenv
```bash
$ sudo -H pip3 install -U pipenv
```
- install libpq-dev
```bash
$ sudo apt install libpq-dev
```
- clone the repo & cd into it
- install dependencies
```bash
$ pipenv install
```


## in case
- generate requirements.txt
```bash
$ pipenv lock -r > requirements.txt
```

## Run with Docker
- Make sure [Docker](https://docs.docker.com/install/ "Docker") & [Docker-Compose](https://docs.docker.com/compose/install/ "Docker-Compose") are installed
- run
```bash
$ docker-compose up -d
```
- exec into the app container and make DB migrations
```bash
$ docker exec -it CONTAINER_ID bash
```
- see app logs
```bash
$ docker logs -f CONTAINER_ID
```
- clean up
```bash
$ docker-compose down -v
```