import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 環境変数から SECRET_KEY を取得。設定されていない場合はエラーにする
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable must be set in production")

# SECURITY WARNING: don't run with debug turned on in production!
# 環境変数から DEBUG を取得。設定されていない場合は False (本番環境)
DEBUG = os.environ.get('DEBUG', 'False') == 'False'

# ALLOWED_HOSTS は Vercel の URL を設定　ローカルでもデバッグできるように修正
ALLOWED_HOSTS = ['yoshi-nakane0-github-io-ai-nexus-studio.vercel.app','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'schedule',
    'prompt',
    'earning',
    'target',
    'control',
    'trending',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise を追加
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject2.urls'

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

WSGI_APPLICATION = 'myproject2.wsgi.application'

# Database
# Vercel でよく使用される PostgreSQL を例として設定
# 環境変数からデータベース情報を取得
# 簡略化のため、SQLiteを使用。PostgreSQLの設定はコメントアウト
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.environ.get('POSTGRES_DB'),
#        'USER': os.environ.get('POSTGRES_USER'),
#        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#        'HOST': os.environ.get('POSTGRES_HOST'),
#        'PORT': os.environ.get('POSTGRES_PORT', '5432'), # PostgreSQLのデフォルトポート
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'  # staticファイルへのURL
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # collectstatic コマンドで収集する場所
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # WhiteNoise

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'