from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('non_active_listings', views.non_active_listings, name='non_active_listings'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("<int:listing_id>/listing", views.listing_page, name="listing_page"),
    path("<int:category_id>/category", views.category_page, name="category_page"),
    path("<int:listing_id>/bid", views.bid_page, name="bid_page"),
    path("<int:listing_id>/add_whatchlist", views.add_whatchlist, name="add_whatchlist"),
    path("<int:listing_id>/remove_whatchlist", views.remove_whatchlist, name="remove_whatchlist"),
    path("<int:listing_id>/close_listing", views.close_listing, name="close_listing"),
    path("<int:listing_id>/new_comment", views.new_comment, name="new_comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories")
]

urlpatterns += staticfiles_urlpatterns()