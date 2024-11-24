"""
URL configuration for POKEDEX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import JsonResponse
import requests

from pokedex_app.views import home, proxy_api, team_detail, zone_post, pokemon_names, zone_get, tournament_get, \
    pokemon_get, list_Pokemons

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pokemonName/<int:id>', pokemon_names, name='names'),
    path('api/events/', zone_post, name='zone_post'),
    path('api/zones/<str:zone_id>/', zone_get, name='zones'),
    path('api/tournaments/<uuid:tournament_id>', tournament_get, name='tournaments'),
    path('api/pokemons/<int:pokemon_id>', pokemon_get, name='pokemons'),
    path('api/<str:endpoint>/', proxy_api, name='proxy_api'),
    path('api/<str:endpoint>/<uuid:team_id>/', team_detail, name='team_detail'),
    path('api/<str:endpoint>/<uuid:zone_id>/', zone_post, name='zone_post'),
    path('pokedex/', list_Pokemons, name='pokedex'),
]
