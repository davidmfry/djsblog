import os
try:
    #
    #  for credit card processing
    #
    from braintree import Environment
except ImportError, e:
    pass

#
#  global for project name replacement
#
PROJECT_NAME = 'djsblog'


#
#  BRAINTREE
#
'''
BRAINTREE_ENV = Environment.Sandbox #@UndefinedVariable
#BRAINTREE_ENV = Environment.Production #@UndefinedVariable
BRAINTREE_MERCHANT = ''
BRAINTREE_PUBLIC_KEY = ''
BRAINTREE_PRIVATE_KEY = ''
'''

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ABSOLUTE_PATH = os.path.dirname( __file__ ).replace( '%s/settings_overrides' % PROJECT_NAME, '' )
FIXTURE_DIRS = ( os.path.join( ABSOLUTE_PATH, 'fixtures', os.environ['ENVIRONMENT'] ).replace('\\','/'), )

#
#  mysql
#
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': {
            #'default-character-set': 'utf8',
            #'default-collation': 'utf8_unicode_ci',
            'init_command': 'SET storage_engine=INNODB',
        },
    },
}
'''

#
#  postgis
#
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'localhost',
        'NAME': 'djsblog',
        'USER': 'gcorradini',
        'PASSWORD': 'gcorradini',
        'OPTIONS': {
            #'autocommit': True,
        },
    },
}

#
#  must match django.contrib.sites
#
SITE_ID = 4

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'minimal': {
            'format': '%(levelname)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        '': {
            'handlers': [ 'console', 'file_logging' ],
            'level': 'DEBUG',
            'propogate': True,
        },
        'django' : {
            'handlers': ['file_logging'],
            'level' : 'DEBUG',
            'propagate' : True,
        },
        'django.db' : {
            'handlers' : ['db_logging'],
            'level' : 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'minimal',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': [ 'require_debug_false' ],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file_logging': {
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'backupCount' : 5,
            'maxBytes': 1024 * 1024 * 5, # 5 mb
            'filename': os.path.join( ABSOLUTE_PATH, '../logs/django.log').replace('\\','/'),
            'formatter': 'verbose',
        },
        'db_logging': {
            'level' : 'ERROR',
            'class' : 'logging.handlers.RotatingFileHandler',
            'backupCount' : 5,
            'maxBytes': 1024 * 1024 * 5, # 5 mb
            'filename': os.path.join( ABSOLUTE_PATH, '../logs/django-db.log').replace('\\','/'),
        },
    },
}

EMAIL_TO='%s@gmail.com' % PROJECT_NAME  # manual configuration
DEFAULT_FROM_EMAIL = '%s_noreply@gmail.com' % PROJECT_NAME # manual configuration
SUPPORT_EMAIL='%s@googlegroups.com' % ( PROJECT_NAME + '_' + os.environ['ENVIRONMENT'] )
SERVER_EMAIL="%s_server@pugetworks.com" % ( PROJECT_NAME + '_' + os.environ['ENVIRONMENT'] )
