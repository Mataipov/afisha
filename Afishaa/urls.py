"""Afishaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from main import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_us/', views.about_us),
    path('', views.index_view),
    path('date_now/', views.date_now),
    path('films/', views.film_list_view),
    path('films/<int:id>/', views.film_detail_view),
    path('director/<int:director_id>/film/', views.director_films),
    path('films/create/', views.create_films),
    path('director/create/', views.create_director),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('search/', views.search_view),
]
