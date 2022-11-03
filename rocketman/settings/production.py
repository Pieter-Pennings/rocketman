import os


from .base import *

DEBUG = False
SECRET_KEY = '0mwv47mwsml1(b@(i89p-5gp5)#oo68itv4ox!_*6c8eq603!q'
ALLOWED_HOSTS = ['localhost', 'mywebsite.com', '*']
cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache"
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'xfHjB^F2p9s*zhqFT6cNx2',
        "HOST": 'localhost',
        "PORT": "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://df3b7643493b46dd827c95d29e377c31@o4504093238886400.ingest.sentry.io/4504093242097664",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
