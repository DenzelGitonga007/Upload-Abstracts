if [[ $CREATE_SUPERUSER ]];
then
  python3 manage.py createsuperuser --no-input
fi
