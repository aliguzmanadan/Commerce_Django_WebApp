from django.contrib import admin
from .models import User, Auction_listing, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Auction_listing)
admin.site.register(Category)