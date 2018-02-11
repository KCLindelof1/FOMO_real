from django import forms
from formlib import Formless
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login
from account.models import User
from account import models as amod
import re


@view_function
def process_request(request):

    # process the form
    form = SignupForm(request)
    if form.is_valid():
        form.commit()
        # once you get here, everything is clean. Don't do more data changes
        # you can no longer inform the user that we have a problem
        print(form.cleaned_data)
        # do the work of the form (ex: make payment, create the user
        return HttpResponseRedirect('/account/index/')

    # render the template
    context = {
        'form': form,
    }
    return request.dmp_render('signup.html', context)


class SignupForm(Formless):

    def init(self):
        # The fields from account/models
        # fname = models.TextField(null=True, blank=True)
        # lname = models.TextField(null=True, blank=True)
        # email = models.Email(null=True, blank=True)
        # birthdate = models.DateTimeField(null=True)
        # address = models.TextField(null=True, blank=True)
        # city = models.TextField(null=True, blank=True)
        # state = models.TextField(null=True, blank=True)
        # zipcode = models.TextField(null=True, blank=True)

        self.fields['fname'] = forms.CharField(label='First Name', required=True)
        self.fields['lname'] = forms.CharField(label='Last Name', required=True)
        self.fields['email'] = forms.EmailField(label='Email', required=True)
        self.fields['age'] = forms.IntegerField(label='Age', required=True)
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput(), min_length=8) # min_length=8, label='Password', required=True)
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput(), min_length=8) # PasswordInput(min_length=8, label='Password 2', required=True)
        self.fields['birthdate'] = forms.DateTimeField(label='Birthdate', required=True)
        self.fields['address'] = forms.CharField(label='Address', required=True)
        self.fields['city'] = forms.CharField(label='City', required=True)
        self.fields['state'] = forms.CharField(label='State', required=True)
        self.fields['zipcode'] = forms.CharField(label='Zipcode', required=True)

    # All our logic to mess with input data should be here:
    def clean_age(self):
        age = self.cleaned_data.get('age')          # already an INT, input came in as a string but then flipped to int by browser
        if age < 18:
            raise forms.ValidationError('You are not 18, please have a parent sign up')
            # don't allow the signup
        return self.cleaned_data

    def clean_birthdate(self):
        return

    def clean_email(self):
        # Ensure email is unique

        return

    def clean_password(self):
        # Ensure that password has 8+ characters, contains a number
        # p = self.cleaned_data.get('password')
        if bool(re.search(r'\d', self.cleaned_data.get('password'))) == False:
            raise forms.ValidationError('You need at least 1 number in your password')
        return self.cleaned_data

    def clean_password2(self):
        # Ensure that password has 8+ characters, contains a number
        # p = self.cleaned_data.get('password')
        if bool(re.search(r'\d', self.cleaned_data.get('password2'))) == False:
            raise forms.ValidationError('You need at least 1 number in your password')
        return self.cleaned_data

    # Catch-all Clean
    def clean(self):
        # Clean the password inputs
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('Please ensure the passwords match.')
        return self.cleaned_data

    def commit(self):
        '''Process form action'''
        # create user object
        self.u1 = amod.User()
        self.u1.first_name = self.cleaned_data.get('fname')
        self.u1.last_name = self.cleaned_data.get('lname')
        self.u1.email = self.cleaned_data.get('email')
        # u1.password = 'password' #This is wrong way to do it
        self.u1.set_password(self.cleaned_data.get('password'))
        self.u1.birthdate = self.cleaned_data.get('birthdate')
        self.u1.address = self.cleaned_data.get('birthdate')
        self.u1.city = self.cleaned_data.get('city')
        self.u1.state = self.cleaned_data.get('state')
        self.u1.zipcode = self.cleaned_data.get('zipcode')

        # save
        self.u1.save()

        # authenticate()
        self.u1 = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))

        # login()
        login(self.request, self.user)

