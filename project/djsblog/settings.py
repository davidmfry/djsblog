import os, sys
import warnings
from django.utils.importlib import import_module

ENVIRONMENT=os.environ.get( 'ENVIRONMENT' )
SERVERVERSION='0.0.1'
BETA = True

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

#
#
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
#
#
USE_I18N = True

#
#
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
#
#
USE_L10N = True

#
#
# If you set this to False, Django will not use timezone-aware datetimes.
#
#
USE_TZ = True

#
# Absolute filesystem path to the project.
#
ABSOLUTE_PATH = os.path.dirname( os.path.dirname( __file__ ) ) + '/'

#
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#
MEDIA_ROOT = os.path.join( ABSOLUTE_PATH, 'media').replace('\\','/')
LOGO_IMAGE_ROOT = os.path.join( 'logos' ).replace('\\','/')

#
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#
MEDIA_URL = '/media/'

#
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#
STATIC_ROOT = ''

#
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
#
STATIC_URL = '/static/'

#
# Additional locations of static files
#
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join( ABSOLUTE_PATH, 'static' ).replace('\\','/'),
)

#
# List of finder classes that know how to find static files in
# various locations.
#
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#
#  secret_key:
#  create one with uuid.uuid4().get_hex()
#
SECRET_KEY='5458a7b2f8fc4fa3b17ff3423e3c985d'

#
# List of callables that know how to import templates from various sources.
#
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    #'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware', 
)

AUTHENTICATION_BACKENDS = ( 
    ( 'profiles.functions.EmailAuthBackend',
      'django.contrib.auth.backends.ModelBackend', )
)

AUTH_PROFILE_MODULE = "profiles.Profile"

ROOT_URLCONF="djsblog.urls"

TEMPLATE_DIRS = (
    os.path.join( ABSOLUTE_PATH, 'templates' ).replace('\\','/'),
    os.path.join( ABSOLUTE_PATH, 'emails' ).replace('\\','/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    # uncomment the next line to enable the admin:
    #
    'django.contrib.admin',

    #
    # for extended manager options
    #
    'django_extensions',

    #
    # for postgis
    #
    #'django.contrib.gis',

    #
    # core apps
    #
    'djsblog',
    'blogengine',
    'django.contrib.comments',
)

DATE_FORMAT = 'N j, Y'
DATE_TIME_FORMAT = 'N j, Y, P'
TIME_FORMAT = 'H:i P'

#
# Mail Server info
#
EMAIL_HOST='localhost'
EMAIL_PORT=25

def override_settings( dottedpath ):
    try:
        _m = import_module( dottedpath )
    except ImportError:
        warnings.warn( "Failed to import environment settings: %s" % dottedpath )
        pass
    else:
        _thismodule = sys.modules[__name__]
        for _k in dir(_m):
            if _k.isupper() and not _k.startswith('__'):
                setattr( _thismodule, _k, getattr( _m, _k ) )

override_settings( 'djsblog.settings_overrides.%s' % os.environ['ENVIRONMENT'] )
