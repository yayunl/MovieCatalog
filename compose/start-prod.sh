#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset



exec /usr/local/bin/gunicorn MovieCatalog.wsgi --bind 0.0.0.0:8000