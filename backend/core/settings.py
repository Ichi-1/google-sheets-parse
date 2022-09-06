from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: don't run with debug turned on in production!
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party apps
    'rest_framework',
    'drf_yasg',
    'apps.google_sheets',
    'celery',
    'corsheaders',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = '/static/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery

CELERY_BROKER_URL = 'redis://redis:6379/0'  
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'  
CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TASK_SERIALIZER = 'json'  


# google api credentials

CREDENTIALS = {
  "type": "service_account",
  "project_id": "parsetable-361616",
  "private_key_id": "da1f8e73d5f19a723a2576847e665b46f3c493f4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDG+sW45l/J2cQS\neaAX1vTbQ+W7QlIZo+eoke0rE/eCbMRnmaqxFbnTDQs8uei6mxJieE4CO+s9vp7t\nO/XFyem0pZGu9Qo7ZY8CGIQV/HySSoxJoqjAx/YSB2bBmtJY/I2ORS9aeTUN8+6l\nJBpOmLlevfy697JQGYWJGE8YvxKzq1uzxdvF2I9Bn95kwVdW+L5vP3VpPlBM04Gf\nnl7eW8zpSz5SmesMCYJaVMquIzsEUq+wiZKIE3LfQtg3UX0ueCSbRvDNx+JxBDj2\nL/9oE/o+y05OieQuEQRPNerC4dB7scfe7RrNrFAdJqBhhceUcwwvGcGLbsxfTOmY\n+7lGvjCJAgMBAAECggEAVzzJBTjTlE7KXQNAAlO3BI7vILuB/UXUIh7gaXuWj3Ma\nZQWFRaBt2S8l1xj3BSFJ3Sw7n1Uf3PE/AmnAZlgRA6d3iMpcExCCs3uGJZGOGCFh\nAkOzUtoYc20VSxqS0HrhoReKHFN5xEVHQtXiRsVEuFn5fQtt/RpDZojm3MWg8G4Q\nfOkIOZcK9IVN72ZkUQb2s+6+FKYnYSZyOWwsJhAzT1bUJQVAzcnNSzkvuFftlfc6\nz6lQOg5BSOiebwrdzLhqeU19aOFrH0HzBCJCR6xQAFTnfV8bNftSRVZuhXWdMEcW\nbZZGMaEv0SB4VNelo+JS42Bd+QcbgUgMfg+jDrSIRQKBgQD7IDUXtyx4PGEk0Iqa\n9sDBl4DUR27pYK5h37hNFQOs92frCrdZsz+nYXpy+rPrFxVPVWzhzuTKZDxWC/oJ\nsY8yHwJ0s7CBZT351wrlITl6V/zaXoijrliOtKwkpfhpGCqfjuph+7DZWHuqNds+\nAq1QOYipn9OHvNlhF7gcmGbkBwKBgQDK13YG4f89Dz1CelQWLlldkQQiGqvln5YT\nqRGYxiR/x+MG6K6nKoY9UzpO/dMHfhN8QL0ONWwtDd/kIjBSTaR75qPGkvg43dOu\nCWcsNBo3FiKbFXt6UAgSztccUH9I2Psgrg3lhUjwH5HwdzO7dWL9sCrhFACDIc8w\nPswWpo7C7wKBgEbJAE4sAqvtkRBYfAlMLm8jLlwnunqsFttdvUx09PFHV5JoFeCB\n5xpeHq7UPeyxN/+Bu8w2jkUCVgOHIraixxNArGeK0uDWUc7fr6GAaPw0WwCOjwNc\nPHgVM0StR8UP28vX8/ckg+fvygPjZGYpSQMJBJ2TgIONVtTIY8wjpTT3AoGBALvk\nd9UKVScXTbSdofRl/KvaX8zDjgWHHTqa+szchgTDgL3unZIFpxF5XeK75lXjaGNJ\niJZ3z/uwBXvKW55xg3KuA3k2vK3YdXOaDDL7FGmAnI+xh46WQdRCOypkOnOdYoo0\nEHVSUGz1oXbwxD/aDddW73FM2OifUc+r69rzb/yLAoGBAKETbzB2NUC6UDorzQGb\n4km5OeIQONVU5c5s04RWbRPmiXpjmLGHp3v/w/eZmnVkN/GVzLIglWMVoEYEPYn1\ndI+RsVPajeFA8H2qxFuNQefbOG4W0nF3rHD2mX+Qkinc3EiWzP81qaGWPBlvAuiP\nmFchdGXWZrF1klTI0WIMWga4\n-----END PRIVATE KEY-----\n",
  "client_email": "parse-table-service-api@parsetable-361616.iam.gserviceaccount.com",
  "client_id": "106478644347189116576",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/parse-table-service-api%40parsetable-361616.iam.gserviceaccount.com"
}


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

CORS_ALLOW_ALL_ORIGINS = True