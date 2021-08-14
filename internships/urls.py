from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', include('User.urls')),
    path('', include('Products.urls')),
    path('admin/', admin.site.urls),
]
