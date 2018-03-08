from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request, cat_id = 0):
    category = cat_id
    cat = cmod.Category.objects.all()
    context = {
        'cat': cat,
        jscontext('category'): category,
        jscontext('pnum'): 1,
    }
    return request.render('index.html', context)

@view_function
def products(request, cat: cmod.Category = None, pnum: int = 1):
    # Load all products into query
    query = cmod.Product.objects.all()
    # Check for category
    if cat is not None:
        query = query.filter(name=cat) # *something like category = cat?*
        page_count = query.count()/6 # *this is pagination, this would get pages 0,1,2,3,4,5*
    return request.dmp.render("index.products.html" ) # *inherits from base_ajax.html*


# need to load all categories into a loop that will put them into an unordered list <ul> as individual list items <li>
cat_list =

for cmod.Product.objects.all()

