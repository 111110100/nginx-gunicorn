#!/bin/bash

kill `pgrep -f "/var/www/app/venv/bin/python3 /var/www/app/venv/bin/gunicorn -c /var/www/app/gunicorn.conf.py --pid=/var/www/app/gunicorn.pid main:app --daemon"`
