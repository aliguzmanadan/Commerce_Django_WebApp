from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.forms import ModelForm

from .models import User, Auction_listing, Category, Bid, Comment
from .forms import ListingForm, BidForm, CommentForm



def index(request):
    return render(request, "auctions/index.html", {
        "Listings": Auction_listing.objects.filter(is_active = True)
    })

def non_active_listings(request):
    return render(request, "auctions/non_active_listings.html", {
        "Listings": Auction_listing.objects.filter(is_active = False)
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        
        if form.is_valid():
            #Isolate the info from the form
            title = form.cleaned_data["title"]
            initial_price = form.cleaned_data["initial_price"]
            description = form.cleaned_data["description"]
            image = form.cleaned_data["image"]
            categories = form.cleaned_data["categories"]

            #Create the new lisitng
            listing = Auction_listing(title=title, initial_price=initial_price, description=description, image=image, creator=request.user)
            listing.save()

            #Add the categories if any
            for category in categories:
                listing.categories.add(category)

            #redirect to index page
            return HttpResponseRedirect(reverse("index")) 

    return render(request, "auctions/create_listing.html", {
        "form": ListingForm()
    })


def listing_page(request, listing_id, wrong_bid=False):
    listing = Auction_listing.objects.get(pk=listing_id)
    return render(request, "auctions/listing_page.html", {
        "listing": listing,
        "in_watch_list": request.user.wishes_per_user.filter(id = listing.id).exists(),
        "comments": listing.comments_by_listing.all(),
        "comment_form": CommentForm(),
        "bid_form": BidForm(), 
        "wrong_bid": wrong_bid
    })


def bid_page(request, listing_id):
    #Recover listing object
    listing = Auction_listing.objects.get(pk=listing_id)

    if request.method == "POST":
        form = BidForm(request.POST)

        if form.is_valid():
            #Isolate the amount from the form
            amount = form.cleaned_data["amount"]

            #if the amount is bigger than the current price, create the bid and return to the listing page
            if amount > listing.current_price():
                new_bid = Bid(amount=amount, listing=listing, user=request.user)
                new_bid.save()
                return HttpResponseRedirect(reverse("listing_page", args=(listing.id,)))

            #if not, send redirect again to the same bidpage with an error message
            else:
                return listing_page(request, listing_id, True)

def add_whatchlist(request, listing_id):
    listing = Auction_listing.objects.get(pk=listing_id)
    listing.in_watch_list.add(request.user)
    return HttpResponseRedirect(reverse("listing_page", args=(listing.id,)))


def remove_whatchlist(request, listing_id):
    listing = Auction_listing.objects.get(pk=listing_id)
    listing.in_watch_list.remove(request.user)
    return HttpResponseRedirect(reverse("listing_page", args=(listing.id,)))

def close_listing(request, listing_id):
    listing = Auction_listing.objects.get(pk=listing_id)
    HighestBid = listing.HighestBid()

    #Checking whter ther is a higest bid
    if HighestBid:
        HighestBidder = HighestBid.user
        listing.winner = HighestBidder

        #making the lisiting non-active
        listing.is_active=False

        #saving updates in the listing
        listing.save()

        #redirect to index page
        return HttpResponseRedirect(reverse("index")) 

    else:
        price = listing.current_price()
        return render(request, "auctions/listing_page.html", {
            "listing": listing,
            "current_price": price,
            "in_watch_list": request.user.wishes_per_user.filter(id = listing.id).exists(),
            "message": "This listing cannot be closed: There are no bids for this listing"
        })


def new_comment(request, listing_id):
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            #isolate the text of the comment
            text = form.cleaned_data["text"]
            #get the listing
            listing = Auction_listing.objects.get(pk=listing_id)

            #create new comment 
            new_comment = Comment(text=text, listing=listing, user = request.user)
            new_comment.save()

            return HttpResponseRedirect(reverse("listing_page", args=(listing.id,))) 

def watchlist(request):
    watchlist = request.user.wishes_per_user.all()
    return render(request, "auctions/watchlist.html",{
        "watchlist": watchlist
    }
    )

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })

def category_page(request, category_id):
    category = Category.objects.get(pk=category_id)
    listings = category.listings_per_category.filter(is_active = True)
    return render(request, "auctions/category_page.html", {
        "category": category,
        "listings": listings
    }) 