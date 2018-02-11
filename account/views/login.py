from django import forms
from formlib import Formless
from account import models as amod
from account.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, RedirectException
import re


@view_function
def process_request(request):

    # process the form
    form = LoginForm(request)
    if form.is_valid():
        form.commit()
        # raise RedirectException('/account/index/')
        return HttpResponseRedirect('/account/index/')

    # render the template
    context = {
        'form': form,
    }
    return request.dmp_render('login.html', context)

class LoginForm(Formless):
    '''Login Form'''

    def init(self):
        self.fields['email'] = forms.CharField(label='Email')
        self.fields['password'] = forms.CharField(label='Password', widget=forms.PasswordInput())
        self.user = None

    def clean(self):
        self.user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid Login information')
        return self.cleaned_data

    def commit(self):
        '''Process Form action'''
        login(self.request, self.user)
        # return HttpResponseRedirect('/account/index')
