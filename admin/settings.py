import os
from pathlib import Path

# Loyihaning bazaviy katalogi
BASE_DIR = Path(__file__).resolve().parent.parent

# Django maxfiy kaliti
SECRET_KEY = 'your-secret-key'

# Django ishlash rejimi
DEBUG = True

# Yashirilgan foydalanuvchilar ro'yxati
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Django ilovalari
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # Sizning dastur (app) nomingiz
]

# Middleware sozlamalari
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL konfiguratsiyalari
ROOT_URLCONF = 'admin.urls'

# Shablonlar sozlamalari
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Agar umumiy shablonlar papkasi bo'lsa
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

# WSGI ilova
WSGI_APPLICATION = 'admin.wsgi.application'

# Ma'lumotlar bazasi sozlamalari
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parol sozlamalari
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

# Xalqaro sozlamalar
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik fayllar sozlamalari
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Agar umumiy statik fayllar papkasi bo'lsa

# settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Bu yerda to'g'ri papka yo'lini ko'rsating


# Media fayllar sozlamalari
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Foydalanuvchi sozlamalari
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
