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
    if product.__class__.__name__ == 'BulkProduct':
        form = EditForm(request, initial={
            'type': product.__class__.__name__,
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': product.price,
            'quantity': product.quantity,
            'reorder_trigger': product.reorder_trigger,
            'reorder_quantity': product.reorder_quantity,
        })
    elif product.__class__.__name__ == 'IndividualProduct':
        form = EditForm(request, initial={
            'type': product.__class__.__name__,
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': product.price,
            'pid': product.pid,
        })
    elif product.__class__.__name__ == 'RentalProduct':
        form = EditForm(request, initial={
            'type': product.__class__.__name__,
            'name': product.name,
            'category': product.category,
            'description': product.description,
            'price': product.price,
            'pid': product.pid,
            'max_rental_days': product.max_rental_days,
            'retire_date': product.retire_date,
        })

    if form.is_valid():
        form.commit(product)
        return HttpResponseRedirect('/manager/productList/')
    context = {
        'form': form,
    }
    return request.dmp.render('editProduct.html', context)


class EditForm(Formless):

    def init(self):
        # all products
        self.fields['type'] = forms.ChoiceField(choices=cmod.Product.TYPE_CHOICES, label='Type', show_hidden_initial=True)
        self.fields['status'] = forms.ChoiceField(choices=cmod.Product.STATUS_CHOICES, label='Status', initial='A')
        self.fields['category'] = forms.ModelChoiceField(queryset=cmod.Category.objects.all(), label='Category')
        self.fields['name'] = forms.CharField(label='Product Name')
        self.fields['description'] = forms.CharField(label='Description')
        self.fields['price'] = forms.DecimalField(label='Price')

        #   bulk products
        self.fields['quantity'] = forms.IntegerField(label='Quantity', required=False)
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False)
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False)

        #   individual / rental
        self.fields['pid'] = forms.CharField(label='Product ID', required=False)

        #   rental product
        self.fields['max_rental_days'] = forms.IntegerField(label='Max Rental Days', required=False)
        self.fields['retire_date'] = forms.DateField(label='Retire Date', required=False)

        self.product = None

    def clean(self):
        type = self.cleaned_data.get('type')
        quantity = self.cleaned_data.get('quantity')
        reorder_trigger = self.cleaned_data.get('reorder_trigger')
        reorder_quantity = self.cleaned_data.get('reorder_quantity')
        pid = self.cleaned_data.get('pid')
        max_rental_days = self.cleaned_data.get('max_rental_days')
        retire_date = self.cleaned_data.get('retire_date')

        print(type)
        print(pid)
        if type == 'IndividualProduct':
            if pid == '':
                raise forms.ValidationError('Individual Product\'s require Product ID')
        elif type == 'BulkProduct':
            if quantity is None:
                raise forms.ValidationError('Quantity is required for Bulk Products')
            if reorder_trigger is None:
                raise forms.ValidationError('Reorder Trigger is required for Bulk Products')
            if reorder_quantity is None:
                raise forms.ValidationError('Reorder Quantity is required for Bulk Products')
        elif type == 'RentalProduct':
            if max_rental_days is None:
                raise forms.ValidationError('Max Rental Days is required for Rental Products')
            if pid == '':
                raise forms.ValidationError('Product ID is required for Rental Products')
        return self.cleaned_data

    def commit(self, product):
        print(product.name)
        type = self.cleaned_data.get('type')
        if type == 'IndividualProduct':
            # product.create_date = self.cleaned_data.get('create_date')
            product.last_modified = self.cleaned_data.get('last_modified')
            product.status = self.cleaned_data.get('status')
            product.name = self.cleaned_data.get('name')
            product.description = self.cleaned_data.get('description')
            product.category = self.cleaned_data.get('category')
            product.price = self.cleaned_data.get('price')
            #   unique fields
            product.pid = self.cleaned_data.get('pid')
        elif type == 'BulkProduct':
            # product.create_date = self.cleaned_data.get('create_date')
            product.last_modified = self.cleaned_data.get('last_modified')
            product.status = self.cleaned_data.get('status')
            product.name = self.cleaned_data.get('name')
            product.description = self.cleaned_data.get('description')
            product.category = self.cleaned_data.get('category')
            product.price = self.cleaned_data.get('price')
            #   unique fields
            product.quantity = self.cleaned_data.get('quantity')
            product.reorder_trigger = self.cleaned_data.get('reorder_trigger')
            product.reorder_quantity = self.cleaned_data.get('reorder_quantity')
        elif type == 'RentalProduct':
            # product.create_date = self.cleaned_data.get('create_date')
            product.last_modified = self.cleaned_data.get('last_modified')
            product.status = self.cleaned_data.get('status')
            product.name = self.cleaned_data.get('name')
            product.description = self.cleaned_data.get('description')
            product.category = self.cleaned_data.get('category')
            product.price = self.cleaned_data.get('price')
            #   unique fields
            product.pid = self.cleaned_data.get('pid')
            product.max_rental_days = self.cleaned_data.get('max_rental_days')
            product.retire_date = self.cleaned_data.get('retire_date')

        product.save()
