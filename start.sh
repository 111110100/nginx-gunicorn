#!/bin/bash

. /var/www/app/venv/bin/activate

GUNICORN=/var/www/app/venv/bin/gunicorn
ROOT=/var/www/app
PID=/var/www/app/gunicorn.pid

APP=main:app

if [ -f $PID ]; then rm $PID; fi

cd $ROOT
exec $GUNICORN -c $ROOT/gunicorn.conf.py --pid=$PID $APP --daemon
