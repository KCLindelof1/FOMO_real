from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function

@view_function
def process_request(request):
    # process the form
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            # once you get here, everything is clean. Don't do more data changes
            # you can no longer inform the user that we have a problem
            print(form.cleaned_data)
            # do the work of the form (ex: make payment, create the user
            return HttpResponseRedirect('/')

    else:
        form = TestForm()

    # render the template
    context = {
        'form': form,
    }
    return request.dmp_render('testform.html', context)


class TestForm(forms.Form):
    favorite_ice_cream = forms.CharField(label='Favorite Ice Cream')
    renewal_date = forms.DateField(label="Renewal", help_text="Enter a date between now and 4 weeks (default 3).")
    age = forms.IntegerField(label="Age")
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()
    widget = forms.PasswordInput        # Try this?


    # All our logic to mess with input data should be here:
    def clean_age(self):
        age = self.cleaned_data.get('age')          # already an INT, input came in as a string but then flipped to int by browser
        if age < 18:
            raise forms.ValidationError('You are not 18, no soup for you')
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
