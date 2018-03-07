from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request):
    context = {
    }
    return request.render('index.html', context)


def products(request, cat: cmod.Category = None, page_num: int = 1):
    # Load all products into query
    query = cmod.Product.objects.all()
    # Check for category
    if cat is not None:
        query = query.filter(…) # *something like category = cat?*
        query = query[0:6] # *this is pagination, this would get pages 0,1,2,3,4,5*
    return request.dmp.render("index.products.html" ) # *inherits from base_ajax.html*
