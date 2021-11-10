from django.forms import ModelForm
from django import forms
from .models import Auction_listing

class ListingForm(ModelForm):
    class Meta:
        model = Auction_listing
        fields = ('title', 'initial_price', 'description', 'image_link', 'categories')

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Title"}),
            'initial_price': forms.NumberInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control", "rows": 3}),
            'image_link': forms.URLInput(attrs={'class': "form-control"}),
            'categories': forms.Select(attrs={'class': "form-control"})
        }