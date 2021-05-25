from ._base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sfifan_db.sqlite3',
    }
}