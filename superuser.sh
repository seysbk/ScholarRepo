#!/bin/bash

echo "from django.contrib.auth import get_user_model
User = get_user_model()
username = '{DJANGO_SUPERUSER_USERNAME}'
email = 'DJANGO_SUPERUSER_EMAIL'
password = '{DJANGO_SUPERUSER_PASSWORD}'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
" | python manage.py shell