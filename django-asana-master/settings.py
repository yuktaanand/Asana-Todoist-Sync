INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'djasana',
]

SECRET_KEY = 'not a secret'
ROOT_URLCONF = 'djasana.urls'

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

MIDDLEWARE = []

DJASANA_WEBHOOK_URL = ' '
DJASANA_WEBHOOK_PATTERN = ''

DEBUG = True

ALLOWED_HOSTS = []

ASANA_CLIENT_ID = '1117024182108892'
ASANA_CLIENT_SECRET = 'd3a2a1e3f86422bd524a081044f9bc0f'
ASANA_OAUTH_REDIRECT_URI = 'https://127.0.0.1:8000/oauth/callback/'
ASANA_ACCESS_TOKEN = '0/92f79995f7c1b4b0f751b9a07c8e52c2'
