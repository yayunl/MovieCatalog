#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py flush --no-input
python manage.py makemigrations movies
python manage.py migrate

if [ "$DEBUG" = 0 ]
then
  echo "Production env."
  python /usr/src/app/manage.py collectstatic --noinput
fi

exec "$@"