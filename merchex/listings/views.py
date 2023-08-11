from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import TitlesBand

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>About</h1> <p>About us page</p>')

def listin(request):
    tit = TitlesBand.objects.all()
    return HttpResponse(f"""<h1> Listings</h1>
                            <p>Titles</p>
                            <ul>
                                <li>{tit[0].title}</li>
                                <li>{tit[1].title}</li>
                                <li>{tit[2].title}</li>
                            </ul>
                        """)

def contact(request):
    return HttpResponse('')