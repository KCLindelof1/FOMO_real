from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod


@view_function
def process_request(request):
    products = cmod.Product.objects.filter(status='A')
    context = {
        'products': products,
    }
    return request.dmp.render('productList.html', context)
