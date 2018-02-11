from django import forms
from formlib import Formless
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login, logout

@view_function
def process_request(request):
    # process the form
        logout(request)
        return HttpResponseRedirect('/homepage/index/')
