from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from .models import Post, Cake, Cupcake, Macaroon, Drink, Galery
from .forms import PostForm

#_________________________________________________

def menufull(request):
    cakes = Cake.objects.all()[:4]
    cupcakes = Cupcake.objects.all()[:4]
    macaroons = Macaroon.objects.all()[:4]
    drinks = Drink.objects.all()[:4]
    return render(request, "cosmocafe/menufull.html",
                  {'cakes': cakes, 'cupcakes': cupcakes, 'macaroons': macaroons, 'drinks': drinks})

def cupcakes(request):
    cupcakes = Cupcake.objects.all()
    return render(request, "cosmocafe/cupcakes.html", {'cupcakes': cupcakes})


def macaroons(request):
    macaroons = Macaroon.objects.all()
    return render(request, "cosmocafe/macaroons.html", {'macaroons': macaroons})


def cakes(request):
    cakes = Cake.objects.all()
    return render(request, "cosmocafe/cakes.html", {'cakes': cakes})


def drinks(request):
    drinks = Drink.objects.all()
    return render(request, "cosmocafe/drinks.html", {'drinks': drinks})


def menu(request):
    return render(request, "cosmocafe/menu.html", {})
#_________________________________________________

def index(request):
    return render(request, "cosmocafe/index.html", {})

def aboutus(request):
    return render(request, "cosmocafe/aboutus.html", {})

def contacts(request):
    return render(request, "cosmocafe/contacts.html", {})

def photogalery(request):
    galery = Galery.objects.all()
    return render(request, "cosmocafe/photogalery.html", {'galery':galery})

def writeus(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/writeus/")
    context={
        "form":form,
    }
    return render(request, "cosmocafe/writeus.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context={
        "name": instance.name,
        "instance": instanse,
    }
    return render(request, "cosmocafe/writeus.html", context )