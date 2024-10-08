import os
from pathlib import Path

# プロジェクトのベースディレクトリを設定
BASE_DIR = Path(__file__).resolve().parent.parent

# 開発環境用のシークレットキー（本番環境では環境変数を使用すること）
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key-replace-in-production')

# デバッグモードを有効化
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# アプリケーションの定義
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rides',
    'debug_toolbar',  # 開発用デバッグツールバー
]

# ミドルウェアの設定
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # 開発用デバッグツールバー
]

ROOT_URLCONF = 'rideshare_projects.urls'

# テンプレートの設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'rideshare_projects.wsgi.application'

# データベースの設定
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 認証設定
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

# 国際化
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# 静的ファイルの設定
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# メディアファイルの設定
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# デフォルトの主キーフィールドの型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 開発用のメール設定
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 開発用のキャッシュ設定
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# ロギング設定
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Debug Toolbar設定
INTERNAL_IPS = ['127.0.0.1']

# 開発環境特有の設定
if DEBUG:
    # ここに開発環境のみで使用する追加の設定を記述
    pass