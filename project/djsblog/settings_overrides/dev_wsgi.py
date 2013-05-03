"""
WSGI config for project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
#
# Add the virtual Python environment site-packages directory to the path
#
import site
site.addsitedir('/srv/www/li259-36.members.linode.com/djblog/venv/pyvenv26/lib/python2.6/site-packages')
#
# Avoid ``[Errno 13] Permission denied: '/var/www/.python-eggs'`` messages
#
import os
os.environ['PYTHON_EGG_CACHE'] = '/srv/www/li259-36.members.linode.com/djblog/project/' + 'djsblog' + '/settings_overrides/egg-cache'
sys.path.append( '/srv/www/li259-36.members.linode.com/djblog/project/' )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djsblog.settings")
os.environ.setdefault("ENVIRONMENT", 'dev' )

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

