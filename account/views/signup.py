from django import forms
from formlib import Formless
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function

@view_function
def process_request(request):

    # process the form
    form = SignupForm(request)
    if form.is_valid():
        # once you get here, everything is clean. Don't do more data changes
        # you can no longer inform the user that we have a problem
        print(form.cleaned_data)
        # do the work of the form (ex: make payment, create the user
        return HttpResponseRedirect('/')

    # render the template
    context = {
        'form': form,
    }
    return request.dmp_render('signup.html', context)


class SignupForm(Formless.Form):

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

        self.fields['fname'] = forms.CharField(label='First Name')
        self.field['lname'] = forms.CharField(label='Last Name')
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['age'] = forms.IntegerField(label='Age')
        # self.fields['password1'] = forms.PasswordInput(label='Password 1')
        # self.fields['password2'] = forms.PasswordInput(label='Password 2')
        self.fields['birthdate'] = forms.DateTimeField(label='Birthdate')
        self.fields['address'] = forms.CharField(label='Address')
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label='State')
        self.fields['zipcode'] = forms.CharField(label='Zipcode')

    # All our logic to mess with input data should be here:
    def clean_age(self):
        age = self.cleaned_data.get('age')          # already an INT, input came in as a string but then flipped to int by browser
        if age < 18:
            raise forms.ValidationError('You are not 18, please have a parent sign up')
            # don't allow the signup
        return age + 1000

    def clean_renewal_date(self):
        return

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('Please ensure the passwords match.')
        return self.cleaned_data
