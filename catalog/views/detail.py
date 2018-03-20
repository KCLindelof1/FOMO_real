from django.http import HttpResponseRedirect, response
from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod
import math


@view_function
def process_request(request, prod_id: cmod.Product, cat_id=0):

    prod = cmod.Product.objects.filter(pid=cat.id)

    prod = prod_id
    img = prod.image_urls()
    category = cat_id
    cat = cmod.Category.objects.all()
    if prod in request.last_five:
        response.last_five.remove(prod)
    request.last_five.insert(0, prod)

    # detail.py
    # product (that they are looking at)
    # remove if current product is already in the list
    # request.last_five.insert(0, product)
    # if length of list > 6 items, remove the last (6)
    # display positions 1 - 5 (so its actually a list of 6)


    # something with cookies here
    # response.set_cookie()
    # request.get_cookie()

    context = {
        'prod': prod,
        'img': img,
        'cat': cat,
    }


    return request.dmp.render('detail.html', context)
