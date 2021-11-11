from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:listing_id>/listing", views.listing_page, name="listing_page"),
    path("<int:listing_id>/bid", views.bid_page, name="bid_page"),
    path("<int:listing_id>/add_whatchlist", views.add_whatchlist, name="add_whatchlist"),
    path("<int:listing_id>/remove_whatchlist", views.remove_whatchlist, name="remove_whatchlist")
]

urlpatterns += staticfiles_urlpatterns()