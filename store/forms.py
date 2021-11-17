from django import forms

from .models import Category, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'stock','category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'category_name'}),
            'description': forms.NumberInput(attrs={'class': 'form-control', 'id': 'description'})
        }