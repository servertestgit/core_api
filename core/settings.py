from .cdn.conf import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_S3_SIGNATURE_VERSION,
    AWS_STORAGE_BUCKET_NAME,
    AWS_ENDPOINT_URL,
    AWS_S3_OBJECT_PARAMETERS,
    DEFAULT_FILE_STORAGE,
    STATICFILES_STORAGE,
)
from pathlib import Path
import os
import environ
from datetime import timedelta
env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

DOMAIN = os.environ.get('DOMAIN')


ALLOWED_HOSTS = ["*"]


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

APPS = [
    'apps.users',
    'apps.authentication',
    'apps.general',
    'apps.video',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'storages',
]

INSTALLED_APPS = DJANGO_APPS + APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# STATIC

# STATIC_ROOT = str(BASE_DIR / "staticfiles")
# STATIC_URL = "/static/"
# STATICFILES_DIRS = [str(BASE_DIR / "static")]


# # MEDIA
# MEDIA_ROOT = str(BASE_DIR / "media")
# MEDIA_URL = "/media/"

DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 2000


AWS_ACCESS_KEY_ID = AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME = AWS_STORAGE_BUCKET_NAME
AWS_S3_ENDPOINT_URL = AWS_ENDPOINT_URL
AWS_S3_OBJECT_PARAMETERS = AWS_S3_OBJECT_PARAMETERS
AWS_LOCATION = AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_EXPIRE = 5
STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATICFILES_STORAGE = STATICFILES_STORAGE
DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE


REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "rest_framework.views.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT', ),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10080),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESFH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}


CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
    # 'https://example.com',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    # 'http://132.39.225.220',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    # 'https://example.com',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    # 'http://132.39.225.220',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    # 'https://example.com',
    'http://127.0.0.1:5173',
    'http://127.0.0.1:8000',
    # 'http://132.39.225.220',
]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = "users.User"
