Guide to setting up a virtualenv for PythonAnywhere Web apps
============================================================

*Yo dawg, we heard you like virtualenvs*...

This site is being served on PythonAnywhere from a virtualenv running Django 1.4

Here's proof: [https://github.com/pythonanywhere/virtualenv_howto](https://github.com/pythonanywhere/virtualenv_howto)

Instructions
------------

Start a Web app using the Manual Config wizard.

*(check it works by visiting the site)*

Start a Bash console

    source virtualenvwrapper.sh
    mkvirtualenv django14

You can check it works -- the prompt should gain the `(django14)` prefix, and
you can check `which pip` returns the virtualenv pip:

    (django14)14:51 ~ $ which pip
    /home/virtualenvdemo/.virtualenvs/django14/bin/pip

Now install Django (1.4):

    pip install django

(apologies if this takes a long time.  We're working on speeding up disk I/O)

Check it worked:

    (django14)15:02 ~ $ which django-admin.py
    /home/virtualenvdemo/.virtualenvs/django14/bin/django-admin.py

Start a new django project:

    django-admin.py startproject mysite

Check it worked:

    (django14)15:02 ~ $ tree mysite
    mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

*(note mysite/mysite folder -- it's definitely 1.4)*

Now edit your wsgi file -- you'll need code like this

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


Now Reload the web app

Go to site -- you should see Django "it worked!"

