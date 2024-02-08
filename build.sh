if [[ $CREATE_SUPERUSER ]];
then
  python3 abstractsys/manage.py createsuperuser --no-input
fi
