"""musicservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music.views import startmusic, addmusic, listmusic, add_to_favorites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listmusic.as_view(), name='main'),
    path('song/<int:id>', startmusic.as_view(), name='song'),
    path('add_to_favorites/', add_to_favorites.as_view(), name='add_to_favorites'),
    path('addmusic/', addmusic.as_view(), name='addmusic'),
]
