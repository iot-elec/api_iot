# api_iot

# App_API
This microservice is the api for using with linux application

## Setup
### Dependency
these are the main dependencies used in the project
- flask 
- flask_migrate
- Flask-Cors
- gunicorn
- pandas
- psycopg2 
- pyjwt
- python-dotenv 
- requests 
- requests-futures


### Environment
To set up your environment, open a terminal and cd to the api directory. You then need to set up a Python virtual environment using
```
// mac or linux
python3 -m venv venv
source venv/bin/activate
// windows
python -m venv venv
venv\Scripts\activate
```
You might have to upgrade pip:
```
(venv)pip install --upgrade pip
```
Then install following dependencies on the requirements file by:
```
(venv) pip install -r requirements.txt
```
You can check whether this is working:
```
(venv) flask run --reload
```
To stop the flask server press Control-C.

## Env file secret 
the URI of the database and jwt is a secret.
Database url is in this format postgresql://username:password@host:port/database


## Run the api on the docker environment
```
(venv) docker-compose up
```
* noted that the the docker compose in this api is for testing purpose only

