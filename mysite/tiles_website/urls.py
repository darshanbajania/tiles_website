from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

app_name = 'tiles_website'

urlpatterns = [
    path('',views.Home_view, name = 'home'),
    path('products/',views.Product_view, name = 'product_page'),
    path('About_us/',views.About_us_view, name = 'about_us_page'),
    path('Contact_us/',views.Contact_us_view, name = 'contact_us_page'),
    path('Login/',views.Login_view, name = 'login_page'),
    path('logout/', LogoutView.as_view(next_page='tiles_website:home'),name="logout_url"),
    path('Dashboard/',views.admin_dashboard_view, name = 'admin_dashboard_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)