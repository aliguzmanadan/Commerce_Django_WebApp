from django.forms import ModelForm
from django import forms
from .models import Auction_listing, Category

class ListingForm(ModelForm):
    class Meta:
        model = Auction_listing
        fields = ('title', 'initial_price', 'description', 'image_link', 'categories')

        labels = {
            "title": "Title", 'initial_price': "Initial price"
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Title"}),
            'initial_price': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "10,00"}),
            'description': forms.Textarea(attrs={'class': "form-control", "rows": 3, 'placeholder': "Add a description"}),
            'image_link': forms.URLInput(attrs={'class': "form-control"}),
            'categories': forms.SelectMultiple(attrs={'class': "form-control"})
        }