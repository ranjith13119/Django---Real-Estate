from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .choices import bedroom_choices, price_choices, state_choices

def index(request):
    
    listings = Listing.objects.filter(is_published = True).order_by('-list_date')

    paginator = Paginator(listings, 1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings" : paged_listings
    }
    
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    querySet_List = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            querySet_List = querySet_List.filter(discribtion__icontains = keywords)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            querySet_List = querySet_List.filter(city__iexact = city)
    
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            querySet_List = querySet_List.filter(state__iexact = state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            querySet_List = querySet_List.filter(betroom__lte = bedrooms)
    
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            querySet_List = querySet_List.filter(price__lte = price)

    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings' : querySet_List,
        'values' : request.GET
    }
    return render(request, 'listings/search.html', context)
