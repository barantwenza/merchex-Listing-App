from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import TitlesBand

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>About</h1> <p>About us page</p>')

def listin(request):
    tit = TitlesBand.objects.all()
    return render(request, 'listings/title.html', {'tit': tit})

def contact(request):
    return HttpResponse('')