# Flask Microservice

Template project for a Flask, Docker microservice

## Get the code
```shell
$ git clone https://github.com/Ilyes-Hammadi/flask-microservice.git
$ cd flask-microservice
```

## Run it locally
```shell
$ pip install -r requirements.txt
$ python app/server.py
```

## Run with docker
```shell
$ docker build -t flask-microservice .
$ docker run -p 5000:80 flask-microservice
```