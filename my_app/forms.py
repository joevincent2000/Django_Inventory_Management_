from django import forms
from .models import Product, Location, ProductMovement

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_id','status')

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location_id','status')

class ProductMovementForm(forms.ModelForm):
    class Meta:
        model = ProductMovement
        fields = ('movement_id', 'from_location', 'to_location', 'product', 'qty')