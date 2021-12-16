#!/usr/bin/env sh
set -eu
/usr/bin/python3.9 manage.py migrate
#exec "$@"