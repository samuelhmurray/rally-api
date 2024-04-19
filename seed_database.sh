#!/bin/bash

rm db.sqlite3
rm -rf ./rallyapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations rallyapi
python3 manage.py migrate rallyapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

