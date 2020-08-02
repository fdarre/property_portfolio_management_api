"""
Django base settings for property_portfolio_management_api project.
Settings shared by all settings files.
"""

import os

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()

###########
# GENERAL
###########

# WSGI application object that Django’s built-in servers (e.g. runserver) will use
WSGI_APPLICATION = "config.wsgi.application"

###############
# APPLICATIONS
###############

DJANGO_APPPLICATIONS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPLICATIONS = ["rest_framework"]

LOCAL_APPLICATIONS = ["properties"]

INSTALLED_APPS = (
    DJANGO_APPPLICATIONS + THIRD_PARTY_APPLICATIONS + LOCAL_APPLICATIONS
)  # noqa F405

##############
# MIDDLEWARES
##############

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#######################
# INTERNATIONALIZATION
#######################

# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

###########
# DATABASE
###########

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db(
        "DATABASE_URL", default="postgres:///django_property_management_api"
    )
}

# Wrap each database operation in a transaction
DATABASES["default"]["ATOMIC_REQUESTS"] = True

#######
# URLS
#######

ROOT_URLCONF = "config.urls"

############
# TEMPLATES
############

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

######################
# PASSWORD MANAGEMENT
######################

PASSWORD_HASHERS = [
    # Argon2 is a nexxt generation hashing algorithm.
    # Requires 'argon2-cffi' third party library.
    # The Password Hashing Competition panel recommends immediate use of Argon2 rather than
    # the other algorithms supported by Django.
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# To prevent Users from choosing poor passwords.
# However, a password passing all the validators doesn’t guarantee that it is a strong password.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

#########
# EMAILS
#########

# The backend used for sending emails
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)

# Specifies a timeout in seconds for blocking operations like the connection attempt.
EMAIL_TIMEOUT = 5

###############
# STATIC FILES
###############

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = BASE_DIR + "staticfiles"

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = "/static/"

##############
# MEDIA FILES
##############

# Absolute path to the directory holding user-uploaded files
MEDIA_ROOT = BASE_DIR + "media"


# URL handling the media served from MEDIA_ROOT
MEDIA_URL = "/media/"

#################
# DJANGO ADDRESS
#################

# Google map Javascript API key
GOOGLE_API_KEY = env("GOOGLE_API_KEY")

########################
# DJANGO REST FRAMEWORK
########################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}