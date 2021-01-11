from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('login/', include('allauth.urls')),
    path('piroquiz/', include('piroquiz.urls')),
    path('', lambda req:redirect('piroquiz:beforehome'), name='root'),
]
