#!/bin/bash

exec /usr/local/bin/gunicorn MovieCatalog.wsgi:application --bind 0.0.0.0:$PORT