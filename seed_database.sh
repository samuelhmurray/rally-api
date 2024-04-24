#!/bin/bash

rm db.sqlite3
rm -rf ./rallyapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations rallyapi
python3 manage.py migrate rallyapi
python3 manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata tokens
python3 manage.py loaddata type
python3 manage.py loaddata community
python3 manage.py loaddata donor
python3 manage.py loaddata need
python3 manage.py loaddata donorneed
