# Create your views here.
import os
from django.shortcuts import render

def home(request):
    with open(os.path.join(os.path.dirname(__file__), 'howto.md')) as f:
        howto = f.read()
    return render(request, 'home.html', dict(howto=howto))