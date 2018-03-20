from django.http import HttpResponseRedirect, response
from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod
import math


@view_function
def process_request(request, prod_id=1):
    
    # something with cookies here
    response.set_cookie()
    request.get_cookie()

    context = {
    }
    return request.dmp.render('detail.html', context)
