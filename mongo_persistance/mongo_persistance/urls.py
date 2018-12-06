from django.contrib import admin

from django.urls import path

from superheroes_site import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('superheroes/<text>/', views.filterhero, name='filterhero'),
    path('superheroes/savehero', views.savehero, name='savehero')
]
