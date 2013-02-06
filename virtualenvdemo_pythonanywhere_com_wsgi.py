# This file contains the WSGI configuration required to serve up your
# web application at http://virtualenvdemo.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# Below are templates for Django and web.py.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload web app' button on the 'Web' tab to make your site
# live.


# +++++++++++ CUSTOM WSGI +++++++++++
# If you have a WSGI file that you want to serve using PythonAnywhere, perhaps
# in your home directory under version control, then use something like this:
#
#import os
#import sys
#
#path = '/home/virtualenvdemo/path/to/my/app
#if path not in sys.path:
#    sys.path.append(path)
#
#from my_wsgi_file import application



# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
activate_this = '/home/virtualenvdemo/.virtualenvs/django14/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

path = '/home/virtualenvdemo/mysite'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

