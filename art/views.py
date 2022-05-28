from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index(request):
    obj = HomeGallery.objects.all()
    return render(request, "art/index.html", {'data': obj})


def collection(request):
    return render(request, "art/collection.html")

def gallery(request):
    obj = Gallery.objects.all()
    return render(request, "art/gallery.html", {'data': obj})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        mail = request.POST['email']
        msg = request.POST['msg']

        obj = Contact(name=name, email=mail, msg=msg)
        obj.save()
        return render(request, "art/index.html")
    else:
        return render(request, "art/contact.html")

def paintings(request):
    obj = Paintings.objects.all()
    return render(request, "art/paintings.html", {'data': obj})

def art_work(request):
    obj = Art_Work.objects.all()
    return render(request, "art/art_work.html", {'data': obj})

def wildlife(request):
    obj = Wildlife.objects.all()
    return render(request, "art/wildlife.html", {'data': obj})

def street_art(request):
    obj = Street_Art.objects.all()
    return render(request, "art/street_art.html", {'data': obj})

def everyday_life(request):
    obj = Everyday_Life.objects.all()
    return render(request, "art/everyday_life.html", {'data': obj})

def history(request):
    obj = History.objects.all()
    return render(request, "art/history.html", {'data': obj})

def nature(request):
    obj = Nature.objects.all()
    return render(request, "art/nature.html", {'data': obj})

def artgallery(request):
    obj = Art_Gallery.objects.all()
    return render(request, "art/art_gallery.html", {'data': obj})

