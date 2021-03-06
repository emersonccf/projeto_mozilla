"""
Django settings for localLibrary project.

Generated by 'django-admin startproject' using Django 3.2.3.

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
SECRET_KEY = 'django-insecure-)#r-sct=a_hi)i)36siwzfni=7wndh*i+xw^&br#^_u3l7u$+&'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django_extensions',  # para realizar importes no shell
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig',  # app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'localLibrary.urls'

# define o caminho para os templates dentro de cada App - raiz onde ficam o
# Projeto e os Apps
SETTINGS_TEMPLATES = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # une a raiz com nome_app e a pasta de templates, o path fica:
            # /catalog/template/catalog
            # o ultimo <catalog> ?? o pr??prio Django que adciona por padr??o
            # para qualquer caminho informado
            # por padr??o, mesmo sem informar este caminho ?? nesta ??rvore de
            # pastas que ele busca os templates
            # o base_generic.html e o index.html ele busca em:
            # /catalog/template
            Path.joinpath(SETTINGS_TEMPLATES, 'catalog', 'templates'),
            Path.joinpath(SETTINGS_TEMPLATES, 'templates'),
        ],
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

WSGI_APPLICATION = 'localLibrary.wsgi.application'

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# define locais opicionais onde buscar arquivos est??ticos  VERIFAR ISSO DEPOIS
STATICFILES_DIRS = [
    "/templates",
]

STATIC_URL = '/static/'
STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Define o controle de sess??o - periodo que o usu??rio pode permanecer logado
SESSION_COOKIE_AGE = 1800  # segundos - equivale 30 minutos
# reinicia a contagem do tempo caso o usuario volte a utilizar o sistema
SESSION_SAVE_EVERY_REQUEST = True

# Define que ao fazer o login ao inv??s de ir para uma p??gina de perfil v?? para
# a p??gina raiz do site
LOGIN_REDIRECT_URL = '/'

# URL para onde o usu??rio ?? redirecionado quando determinada p??gina necessita
# de autentica????o por login e senha
LOGIN_URL = '/accounts/login/'

# Permite testar o envio de e-mail no ambiente de desenvolvimento,
# enviando mensagens para o console do Django
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
