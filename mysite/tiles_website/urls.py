from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tiles_website'

urlpatterns = [
    path('',views.Home_view, name = 'home'),
    path('products/',views.Product_view, name = 'product_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)