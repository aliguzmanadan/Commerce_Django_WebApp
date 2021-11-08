from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BooleanField, CharField, FloatField, TextField, URLField
from django.db.models.fields.related import ForeignKey, ManyToManyField


class User(AbstractUser):
    pass

class Category(models.Model):
    title = CharField(max_length=64)

class Auction_listing(models.Model):
    title = CharField(max_length=64)
    initial_price = FloatField()
    description = TextField(blank=True)
    creator = ForeignKey(User, on_delete=models.CASCADE, related_name="created_listings")
    winner = ForeignKey(User, on_delete=models.CASCADE, related_name="won_listings", blank=True)
    is_active = BooleanField(default=True)
    image_link = URLField(max_length=500, blank=True)
    categories = ManyToManyField(Category, blank=True, related_name="listings_per_category")
    in_watch_list = ManyToManyField(User, blank=True, related_name="wishes_per_user")

class Bid(models.Model):
    amount = FloatField()
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="bids_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='bids_by_user')

class Comment(models.Model):
    text = TextField()
    listing = ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="comments_by_listing")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="comments_by_user")
