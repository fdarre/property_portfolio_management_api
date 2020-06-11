"""
Production specific settings.
"""

from .base import *  # noqa
from .base import env

##########
# GENERAL
##########

DEBUG = False

###########
# SECURITY
###########

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

###########
# DATABASE
###########

DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405


#################
# ADMINISTRATION
#################

ADMIN_URL = env("DJANGO_ADMIN_URL")
