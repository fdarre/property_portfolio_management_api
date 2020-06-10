"""
Development specific settings.
"""

from .base import *

##########
# GENERAL
##########

DEBUG = True

###########
# SECURITY
###########
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="4&*my70ml*v+$5q&14b#s8owqnc0u^8pwzz*9k+)t#jm-(ctw@"
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

#########
# EMAILS
#########

# The backend used for sending emails
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

#######################
# django-debug-toolbar
#######################
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
