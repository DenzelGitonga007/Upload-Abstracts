#!/usr/bin/env bash
# exit on error
# Change build to ./build.sh
# set -o errexit

# pip install -r requirements.txt

# python manage.py collectstatic --no-input
# python manage.py migrate

# Create a superadmin
# if [[ $CREATE_SUPERUSER ]];
# then
#   python manage.py createsuperuser --no-input
# fi




# Go to the dashboard of the project and create the following environment variables:

# Key = Value
# -----------------
# CREATE_SUPERUSER = True
# DJANGO_SUPERUSER_EMAIL = <...>
# DJANGO_SUPERUSER_PASSWORD = <...>
# DJANGO_SUPERUSER_USERNAME =<...>
# After that add the following to this build.sh script:

# if [[ $CREATE_SUPERUSER ]];
# then
#   python world_champ_2022/manage.py createsuperuser --no-input
# fi
# Commit and push your changes