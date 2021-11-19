from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Auction_listing, Bid, Category, Comment

class ListingForm(ModelForm):
    class Meta:
        model = Auction_listing
        fields = ('title', 'initial_price', 'description', 'image', 'categories')

        labels = {
            'title': "Title*",
            'initial_price': "Initial price*",
            'description': "Description*",
            'image': "Link for the image (optional)",
            'categories': "Select categories (optional)"
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Title"}),
            'initial_price': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "10,00"}),
            'description': forms.Textarea(attrs={'class': "form-control", "rows": 3, 'placeholder': "Add a description"}),
            'image': forms.ClearableFileInput(attrs={'class': "form-control"}),
            'categories': forms.SelectMultiple(attrs={'class': "form-control"})
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ('amount',)
        labels = {
            'amount': ""
        }
        widgets = {
            'amount': forms.NumberInput(attrs={'class': "form-control", 'placeholder': "New Bid"})
        }

class CommentForm(ModelForm):
    class Meta: 
        model = Comment
        fields = ('text',)
        labels = {
            'text': ""
        }
        widgets = {
            'text': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Insert here your comment..."})
        }