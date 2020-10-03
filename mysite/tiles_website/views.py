from django.shortcuts import render, redirect
from .models import Product_tile, Home_page_images
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Home_view(request):
    carousal_images = Home_page_images.objects.all().first()
    context = {
        'home_images' : carousal_images,
    }
    print(type(carousal_images))
    return render(request, 'tiles_website/base.html', context)

def Product_view(request):
    return render(request, 'tiles_website/products.html')

def About_us_view(request):
    return render(request, 'tiles_website/about_us.html')

def Contact_us_view(request):
    return render(request, 'tiles_website/contact_us.html')

def Login_view(request):

    # if session is there redirect to profile page
    if request.session.has_key('is_logged_in'):
        return redirect('tiles_website:home')
        
    if request.method == 'POST':  # authanticate user using login page

        # getting the username of current user
        username = request.POST.get('username')
        # getting the password of current user
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        # authenticating current user
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:  # A backend authenticated the credentials
            login(request, user)  # logging in the current user
            # make the session true after logging in
            request.session['is_logged_in'] = True
  # if user is admin redirect it to admin_page
            return redirect('tiles_website:home')

        else:
            # No backend authenticated the credentials
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')

def admin_dashboard_view(request):
    return render(request, 'tiles_website/admin_dashboard.html')