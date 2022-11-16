from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('pie', 'firstName', 'secondName', 'address',
                  'city', 'postcode', 'deliverDate', 'comments')
        labels = {
            'pie': 'Pie',
            'firstName': 'First Name',
            'secondName': 'Second Name',
            'adress': 'Adress',
            'city': 'City',
            'postcode': 'Postcode',
            'deliverDate': 'Delivery date',
            'comments': 'Any comments to the order',
        }
        widgets = {'deliverDate': forms.DateTimeInput(attrs={"type": "datetime-local"}),
                   'pie':forms.HiddenInput(attrs={"id": "pie-selector"})}
