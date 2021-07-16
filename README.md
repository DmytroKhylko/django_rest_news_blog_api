## Django News Blog API

#### All necessary variables are stored in ***.env*** file in api top level directory
##### ***.env*** example
```
HOST=0.0.0.0
PORT=8000
POSTGRES_DB_HOST=db
POSTGRES_DB_PORT=5432
POSTGRES_DB_NAME=postgres
POSTGRES_DB_USER=postgres
POSTGRES_DB_PASSWORD=1234
```
#### To run API run:
```
docker-compose up
```
#### Migrations are automatically performed on each lounch 
#### To perform manual migrations run
```
python manage.py makemigrations
python manage.py migrate
```
#### Postman collection for basic interaction with API
```[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/b38f85a1cc5ae50cce15?action=collection%2Fimport#?env%5BNews_blog_environment%5D=W3sia2V5IjoiRU1BSUwiLCJ2YWx1ZSI6InNvbWVAZW1haWwuY29tIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJQQVNTV09SRCIsInZhbHVlIjoic29tZV9wYXNzd29yZCIsImVuYWJsZWQiOnRydWV9LHsia2V5IjoiSldUX1RPS0VOIiwidmFsdWUiOiJleUowZVhBaU9pSktWMVFpTENKaGJHY2lPaUpJVXpJMU5pSjkuZXlKMGIydGxibDkwZVhCbElqb2lZV05qWlhOeklpd2laWGh3SWpveE5qSTJOREV5TmprMkxDSnFkR2tpT2lJNFpUVXdOMlUyTURNelpHRTBNV05oWVRFeVkyTmlaV0U0WlROallUYzNOeUlzSW5WelpYSmZhV1FpT2pGOS5RMkVkd2hNaXp2LWEtclBtYlpHY28xcFotUDFuOFRYczFNNjlQVEdHMjhRIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJVUkwiLCJ2YWx1ZSI6ImRqYW5nby1uZXdzLWJsb2ctdGVzdC5oZXJva3VhcHAuY29tIiwiZW5hYmxlZCI6dHJ1ZX1d)```
#### Heroku Link
https://django-news-blog-test.herokuapp.com/
