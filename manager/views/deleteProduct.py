from django import forms
from django.conf import settings
from django_mako_plus import view_function, jscontext
from django.http import HttpResponseRedirect
from datetime import datetime, timezone
from formlib import Formless
from django.forms.models import model_to_dict
from catalog import models as cmod


@view_function
def process_request(request, product: cmod.Product):
    product.status = 'I'
    product.save()
    return HttpResponseRedirect('/manager/productList/')
