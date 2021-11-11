from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import fields
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, DecimalField, FloatField, TextField, URLField
from django.db.models.fields.related import ForeignKey, ManyToManyField



class User(AbstractUser):
    pass

class Category(models.Model):
    title = CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"

class Auction_listing(models.Model):
    title = CharField(max_length=64)
    initial_price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField(blank=True)
    creator = ForeignKey(User, on_delete=models.CASCADE, related_name="created_listings")
    winner = ForeignKey(User, on_delete=models.CASCADE, related_name="won_listings", blank=True, null=True)
    is_active = BooleanField(default=True)
    image_link = URLField(max_length=500, blank=True)
    categories = ManyToManyField(Category, blank=True, related_name="listings_per_category")
    in_watch_list = ManyToManyField(User, blank=True, related_name="wishes_per_user")

    def __str__(self):
        return f"{self.title}, initial price: {self.initial_price}, creator: {self.creator}"

class Bid(models.Model):
    amount = FloatField()
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="bids_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='bids_by_user')

class Comment(models.Model):
    text = TextField()
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="comments_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="comments_by_user")

