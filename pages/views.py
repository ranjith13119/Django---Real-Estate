from django.shortcuts import render
# from django.http import HttpResponse
from listings.choices import bedroom_choices, price_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.filter(is_published = True).order_by('-list_date')[:3]
    context = { 
        'listings' : listings,
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    is_mvp = Realtor.objects.all().filter(is_mvp = True)
    context = {
        "realtors" : realtors,
        "mvp_realtors" : is_mvp
    }
    return render(request, 'pages/about.html', context)
