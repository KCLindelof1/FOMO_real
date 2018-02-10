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
