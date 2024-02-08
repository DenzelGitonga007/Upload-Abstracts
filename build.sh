#!/usr/bin/env bash
# exit on error
# Change build to ./build.sh
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Create a superadmin
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input
fi
