from django.contrib import admin
from .models import User, Auction_listing, Category, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_listing)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)