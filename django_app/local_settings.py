import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


SECRET_KEY = 'j7ZpeG04d/l7fUQKGUJUTPzDtx8aBfnKe4K8tRz2'



DEBUG = True