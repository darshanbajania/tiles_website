from django.urls import path, include
from . import views

app_name = 'tiles_website'

urlpatterns = [
    path('',views.Home_view, name = 'home'),
]