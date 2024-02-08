if [[ $CREATE_SUPERUSER ]];
then
  python abstractsys/manage.py createsuperuser --no-input
fi
