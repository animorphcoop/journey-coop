try:
    from .local import *
except ImportError:
    pass

from .base import *


DEBUG = True

SECRET_KEY = 'django-insecure-xe*tvqiv747y*^w$2=r2l3)_^!phd&ylp%yq)bm1hre1=g2*=y'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
INSTALLED_APPS += [
    'django_browser_reload',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
    "django_browser_reload.middleware.BrowserReloadMiddleware",

]

INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_CONFIG = {
    "ROOT_TAG_EXTRA_ATTRS": "hx-preserve"
}

# PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'journey_db_dev',
        'USER': 'journey_user_dev',
        'PASSWORD': 'local_testing_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }}

