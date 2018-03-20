# from django.http import HttpResponseRedirect
# from django_mako_plus import view_function, jscontext
# from datetime import datetime
# from catalog import models as cmod
# import math
#
#
# @view_function
# def process_request(request, cat_id=0, pNum=1):
#     category = cat_id
#     cat = cmod.Category.objects.all()
#
#     context = {
#         'cat': cat,
#         jscontext('category'): category,
#     }
#     return request.dmp.render('index.html', context)
