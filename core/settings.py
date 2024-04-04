from datetime import timedelta
import os
from pathlib import Path
import logging.config
import urllib.parse
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = bool(os.environ.get("DEBUG", default=1))

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# Application definition

THIRD_PARTY_APPS = [
    "django_filters",
    "django_htmx",
    # "django_fastdev"
]

LOCAL_APPS = [
    "users",
    "workout",
]

INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ] + THIRD_PARTY_APPS + LOCAL_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middlewares.RequestResponseLoggerMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            'debug': DEBUG,
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# ---------------------------------MEDIA AND STATIC ROOT AND URL-------------------------------------------------#
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATIC_DIR = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# ---------------------------------STATICFILES_DIRS-------------------------------------------------#
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files_custom"),
]

# ---------------------------------DEFAULT PRIMARY KEY FIELD TYPE-------------------------------------------------#
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------------------------Auth User-------------------------------------------------#
AUTH_USER_MODEL = "users.User"

# ----------------------------------------------LOGGING SETTINGS------------------------------------------------------
LOGGING_CONFIG = None  # This empties out Django's logging config

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": True,
#     "formatters": {
#         "simple": {
#             "format": "%(levelname)s %(message)s",
#             "datefmt": "%y %b %d, %H:%M:%S",
#         },
#     },
#     "handlers": {
#         "console": {
#             "level": "DEBUG",
#             "class": "logging.StreamHandler",
#             "formatter": "simple",
#         },
#         "celery": {
#             "level": "DEBUG",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": "celery.log",
#             "formatter": "simple",
#             "maxBytes": 1024 * 1024 * 100,  # 100 mb
#         },
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": "debug.log",
#             "maxBytes": 1024 * 1024 * 100,  # 100 mb
#         },
#     },
#     "loggers": {
#         "celery": {
#             "handlers": ["celery", "console"],
#             "level": "DEBUG",
#         },
#         "django": {
#             "handlers": ["file", "console"],
#             "level": "INFO",
#             "propagate": True,
#         },
#         "info_logger": {
#             "level": "INFO",
#             "handlers": ["file", "console"],
#         }
#     },
# }

# logging.config.dictConfig(LOGGING)


# ----------------------------------------------EMAIL SETTINGS------------------------------------------------------
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", True)
EMAIL_PORT = os.environ.get("EMAIL_PORT", 1025)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "your-username")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "your-password")

# ---------------------------------------------REDIS SETTINGS------------------------------------------------------
REDIS_HOST = "redis_server"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = "redis-password"

# ---------------------------------------------CELERY SETTINGS------------------------------------------------------
encoded_password = urllib.parse.quote_plus(REDIS_PASSWORD)
CELERY_BROKER_URL = f"redis://:{encoded_password}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
CELERY_RESULT_BACKEND = (
    f"redis://:{encoded_password}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Kathmandu"


# ---------------------------------------------CORS SETTINGS------------------------------------------------------
ALLOWED_HOSTS = ["*"]


# ---------------------------------------------SESSION SETTINGS------------------------------------------------------
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365 * 10  # 10 years
