from django.contrib import admin #type:ignore
from django.urls import path #type:ignore
from .views.main_views import home, create_blog, edit_blog, single_blog
from .views.auth_views import login, register


urlpatterns = [
   path('', home),
   path('register/',register),
   path('login/',login),
   path('create/',create_blog),
   path('edit/',edit_blog),
   path('single/',single_blog),
]