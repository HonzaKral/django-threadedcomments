import os

DEFAULT_CHARSET = 'utf-8'

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'threadedcomments_test.db')

ROOT_URLCONF = 'threadedcomments.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'threadedcomments',
)