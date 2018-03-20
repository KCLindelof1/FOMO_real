from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime
from catalog import models as cmod
import math


@view_function
def process_request(request, cat_id=0, pNum=1):
    category = cat_id
    cat = cmod.Category.objects.all()
    if category != 0:
        page = cmod.Product.objects.filter(category_id=cat_id).count()
    else:
        page = cmod.Product.objects.all().count()
    page = page/6
    page = math.ceil(page)

    currentPage = page

    context = {
        'cat': cat,
        jscontext('category'): category,
        jscontext('pNum'): pNum,
        jscontext('pMax'): page,
        'currentPage': currentPage,
    }
    return request.dmp.render('index.html', context)

@view_function
def products(request, cat: cmod.Category=None, pNum: int=1):
    # qry = cmod.Product.objects.all()

    if cat is not None:
        qry = cmod.Product.objects.filter(category_id=cat.id)
        cName = cat
    else:
        qry = cmod.Product.objects.all()
        cName = 'All Products'

    pMax = qry.count()/6
    pMax = math.ceil(pMax)
    qry = qry[((pNum - 1)*6):6*pNum] #pagination

    if (pNum < 1) | (pNum > pMax):
        # raise RedirectException('/catalog/index.products.html/')
        return HttpResponseRedirect('/catalog/index.products.html/')

    context = {
        'qry': qry,
        'cName': cName,
        'pNum': pNum,
        'pMax': pMax,
    }
    return request.dmp.render('index.products.html', context) #inherits from base_ajax
# this is a test comment
