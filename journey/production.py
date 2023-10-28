try:
    from .local import *
except ImportError:
    pass

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }}

DEBUG = False
DJANGO_VITE_DEV_MODE = False
