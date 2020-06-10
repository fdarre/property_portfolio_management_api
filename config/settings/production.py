"""
Production specific settings.
"""

from .base import *

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

DATABASES["default"] = env.db("DATABASE_URL")
DATABASES["default"]["ATOMIC_REQUESTS"] = True


#################
# ADMINISTRATION
#################

ADMIN_URL = env("DJANGO_ADMIN_URL")
