"""
Django settings for onlinexam project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
MEDIA_ROOT=os.path.join(BASE_DIR,'static')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@k0#p3kidu)yaaa3u1hplxz)f@^6xiy384*(+n@@s5x#1bx@m5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exam',
    'teacher',
    'student',
    'widget_tweaks',
    'djongo',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_COOKIE_SECURE=False
ROOT_URLCONF = 'onlinexam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'onlinexam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases




import dj-database-url
import os
DATABASES = {
	"default": dj_database_url.parse(os.environ.get("postgres://ungraduate_coders_user:QDv04TD9oZNLT3DEHYQJ5e4XRZBsEubn@dpg-cl6a7rhk857s73cqa7p0-a.singapore-postgres.render.com/ungraduate_coders"))
}

















# import ssl

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'Dehradun',  
#         'CLIENT': {
#             'host': 'mongodb+srv://EduExamGuru:gulshan@cluster0.ok0bgkw.mongodb.net/?ssl=true',
#             'username': 'EduExamGuru',
#             'password': 'gulshan',
#         }
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'Dehradun',  # Replace with your MongoDB database name
#         'ENFORCE_SCHEMA': False,
#         'CLIENT': {
#             'host': 'mongodb+srv://nstidehradun:dehradun@cluster0.ok0bgkw.mongodb.net/',
#             'username': 'nstidehradun',
#             'password': 'dehradun',
#          
#       
#         }
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR ,'db.sqlite3'),
#     }
# }





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




STATIC_URL = '/static/'

STATICFILES_DIRS=[
STATIC_DIR,
 ]

LOGIN_REDIRECT_URL='/afterlogin'


EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bubugulshan509@gmail.com' 
EMAIL_HOST_PASSWORD = 'uwvr nems ddsi jlsg' 
EMAIL_RECEIVING_USER = ['kunjeshyadav7488@gmail.com']
