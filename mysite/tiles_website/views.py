from django.shortcuts import render, redirect

# Create your views here.

def Home_view(request):
    return render(request, 'tiles_website/base.html')

def Product_view(request):
    return render(request, 'tiles_website/products.html')