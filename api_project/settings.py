"""
Django settings for api_project project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4=fa6bksstpw@5lhytjj!n^bfg4eq4a@oq78%p1q3x^_qe+=b&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# добавляем адреса, с которых будет возможен запрос. Теперь сервер будет отвечать
# на запросы с http://localhost:3000, на котором располагается тестовый front-end сервер.
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # до 10-го урока
    # 'graphene_django',

    'rest_framework',
    'rest_framework.authtoken',
    'userapp',
    'corsheaders',
    'todoapp',
    'django_filters',
    'drf_yasg'

]

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

ROOT_URLCONF = 'api_project.urls'

# http://127.0.0.1:8000/api/users/1/
# http://127.0.0.1:8000/api/2.0/users/1/

REST_FRAMEWORK = {
    'DEFAULT_RENDER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 100,
    'DEFAULT_PERMISSION_CLASSES': [
        # все запросы доступны только авторизованным пользователям
        # 'rest_framework.permissions.IsAuthenticated',
        # включим временно для тестов IsAuthenticatedOrReadOnly
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # базовоя — для возможности зайти с логином и паролем;
        'rest_framework.authentication.BasicAuthentication',
        # в сессии — для работы внутренней части сайта, стандартной админки и DRF в браузере.
        # 'rest_framework.authentication.SessionAuthentication',
        # по токену — для работы на стороне клиента и для удобной и безопасной работы с API;
        'rest_framework.authentication.TokenAuthentication',
    ],

    # При использовании UrlPathVersioning мы можем передать номер версии в URL-адресе
    # для 'DEFAULT_VERSIONING_CLASS' не использовать словарь настроек, проблемы с парсингом
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # HostNameVersioning - позволяет указать версию в имени хоста, например "http://v1.example.com/bookings/", исп. на боевом сервере
    # QueryParameterVersioning - позволяет указывать версии в качестве его параметра, например:
    # http://127.0.0.1:8000/api/users/?version=v2
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.QueryParameterVersioning',
    # Указание версии в заголовках запроса - AcceptHeaderVersioning
    # http://127.0.0.1:8000/api/users/
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.AcceptHeaderVersioning'

}
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDER_CLASSES'].append('rest_framework.permissions.BrowsableAPIRenderer')

# до 10-го урока
# GRAPHENE = {
#     "SCHEMA": "userapp.schema.schema"
# }

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

WSGI_APPLICATION = 'api_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

"""https://stackoverflow.com/questions/49189402/auth-user-groups-fields-e304-reverse-accessor-for-user-groups-clashes-with"""
AUTH_USER_MODEL = 'userapp.APIUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# SWAGGER_SETTINGS = {
#    'DEFAULT_INFO': 'import.path.to.urls.api_info',
# }