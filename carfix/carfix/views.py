from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
    # return HttpResponse("Hello, world. You're at the index.")


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contect(request):
    return render(request, 'contect.html')

def review(request):
    return render(request, 'review.html')

def caseList(request):
    return render(request, 'caseList.html')


def caseDetail(request):
    return render(request, 'caseDetail.html')


def ourTeam(request):
    return render(request, 'ourTeam.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')
    

