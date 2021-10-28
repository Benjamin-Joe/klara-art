from django.contrib import admin
from django.urls import path, include

# Urls.py main file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]
