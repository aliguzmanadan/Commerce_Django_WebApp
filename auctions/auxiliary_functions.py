
def current_price(listing):
    #getting all bids for the listing
    bids = listing.bids_by_listing.all()
    if bids:
        #Take all bids amounts and return the hihgest
        amounts = [bid.amount for bid in bids]
        return max(amounts)
    else: 
        return listing.initial_price