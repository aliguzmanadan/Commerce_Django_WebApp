from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DecimalField, FloatField, TextField, URLField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.db.models import Max



class User(AbstractUser):
    def AmountWatchlist(self):
        return self.wishes_per_user.count()



class Category(models.Model):
    title = CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

    def AmountOfListings(self):
        return self.listings_per_category.count()

class Auction_listing(models.Model):
    title = CharField(max_length=64)
    initial_price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(blank=True)
    creator = ForeignKey(User, on_delete=models.CASCADE, related_name="created_listings")
    winner = ForeignKey(User, on_delete=models.CASCADE, related_name="won_listings", blank=True, null=True)
    is_active = BooleanField(default=True)
    #image_link = URLField(max_length=500, blank=True)
    categories = ManyToManyField(Category, blank=True, related_name="listings_per_category")
    in_watch_list = ManyToManyField(User, blank=True, related_name="wishes_per_user")
    image = models.ImageField(
        upload_to='images/', 
        blank=True, 
        null=True,
        editable=True
        )


    def __str__(self):
        return f"{self.title}, initial price: {self.initial_price}, creator: {self.creator}"

    def HighestBid(self):
        '''Returns the higest bid for a listing'''
        if self.bids_by_listing.exists():
            max_bids_amount = self.bids_by_listing.all().aggregate(Max('amount'))['amount__max']
            return self.bids_by_listing.all().get(amount = max_bids_amount)
        else:
            return None

    def current_price(self):
        if self.HighestBid():
            return self.HighestBid().amount
        else:
            return self.initial_price

    def AmountOfBids(self):
        return self.bids_by_listing.count()

    def AmountOfComments(self):
        return self.comments_by_listing.count()
        

class Bid(models.Model):
    amount = DecimalField(max_digits=10, decimal_places=2)
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="bids_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='bids_by_user')

    def __str__(self):
        return f"Bid from {self.user} on {self.listing.title}, created by {self.listing.creator}"

class Comment(models.Model):
    text = TextField()
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="comments_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="comments_by_user")

    def __str__(self):
        return f"Comment: {self.id}, User: {self.user}, on listing: {self.listing.title} "

