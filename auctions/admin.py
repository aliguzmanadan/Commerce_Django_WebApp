from django.contrib import admin
from .models import User, Auction_listing, Category, Bid, Comment

# Register your models here.
class Auction_listingAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "initial_price", "creator", "is_active")


admin.site.register(User)
admin.site.register(Auction_listing, Auction_listingAdmin)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)