FROM python:3.9-buster
RUN mkdir /usr/src/api/
COPY . /usr/src/api/
WORKDIR /usr/src/api
RUN pip install -r requirements.txt
RUN chmod +x ./wait-for-it.sh
RUN chmod +x init.sh
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver