from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.models import Band
from listings.models import TitlesBand
from listings.Forms import BandForm, ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method =='POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #create a new 'Band' and save it to the db
            band = form.save()
            #redirect to the detail page of the band we just created
            #we can provide the url pattern arguments as arguments to redirect function
            return redirect('band-detail', band.id)

    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form':form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # update the existing 'Band' in the db
            form.save()
            # redirect to the detail page of the 'Band' we just updated
            return redirect ('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form':form})

def band_delete(request, id):
    band = Band.objects.get(id=id) # we need this for both GET and POST
    if request.method == 'POST':
        # delete the band from the database
        band.delete()
        return redirect('band_list')
    
    # no need for an 'else' here. if it's a GET request just continue
    
    return render(request, 'listings/band_delete.html', {'band':band})


def about(request):
    return HttpResponse('<h1>About</h1> <p>About us page</p>')

def listin(request):
    tit = TitlesBand.objects.all()
    return render(request, 'listings/title.html', {'tit': tit})

def contact(request):
    if request.method =='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject = f'Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form',
                message = form.cleaned_data['email'],
                from_email = form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz'],
            )
            return redirect('email-sent')
        
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})