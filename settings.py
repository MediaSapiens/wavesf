# -*- coding: utf-8 -*-
# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/')

#applications
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps/externals'))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications/libs'))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications/externals'))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'applications/internals'))

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djangotoolbox',
	'registration',
	'gadget',
	#'easy_thumbnails',
	#'guardian',
	#'userena',
    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'lsettings.disable.DisableCSRF'
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
LANGUAGES = (('de', 'German'),
             ('en', 'English'))
USE_I18N = True

SITE_ID = 3

#============== APPS EXT====================

#giga + userena
GIGYAUTH_API_KEYS = '2_qIePKPJ_T-NIHQ0_JpdNrhUgj7-B7YmCkeqIus1U68S8ElsLsN5BQOtTnhvX6nYg'
#localhost:808
#'2_ZVBWfZFQwm2ovDUJ1lJWtQKq7J1Gr3nCMfC2_g3FNiYd37lhrtEot6T4M1JianRD'

AUTHENTICATION_BACKENDS = (
    #'userena.UserenaAuthenticationBackend',
    #'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
	#'gigyauth.backends.gigyaoauth.GigyaBackend',
)
AUTH_PROFILE_MODULE = False
USERENA_MUGSHOT_GRAVATAR = False
#guardian
LOGIN_REDIRECT_URL = '/'
ANONYMOUS_USER_ID = -1

#registration
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.



# Activate django-dbindexer if available
try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
    DBINDEXER_SITECONF = 'dbindexes'
    MIDDLEWARE_CLASSES = ('dbindexer.middleware.DBIndexerMiddleware',) + \
                         MIDDLEWARE_CLASSES
except ImportError:
    pass
