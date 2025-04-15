#!/bin/sh

python ./manage.py migrate
python ./manage.py collectstatic --no-input -c
#python ./manage.py crontab add
gunicorn config.wsgi:application --workers=3 --bind 0.0.0.0:8000
