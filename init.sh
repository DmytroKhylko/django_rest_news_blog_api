python manage.py makemigrations
python manage.py migrate
python resetupvotes.py &
python manage.py runserver 0.0.0.0:$PORT --noreload