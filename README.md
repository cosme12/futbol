# futbol


## Django commands

### Run server

```python manage.py runserver```

### Create new app

1. ```python manage.py startapp newapp```

### Migrations


1. Create or update a model
2. Run ```./manage.py makemigrations <app_name>```
3. Run ```./manage.py migrate``` to migrate everything or ```./manage.py migrate <app_name>``` to migrate an individual app
4. Repeat as necessary


## Production

### Static files production

https://docs.djangoproject.com/en/2.2/howto/static-files/
https://stackoverflow.com/questions/12042202/django-static-files-not-working