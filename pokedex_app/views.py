from django.shortcuts import render

from pokedex_app.models import pokemon


# Create your views here.
def home(request):
    pokemons = pokemon.objects.all()
    context={
        pokemons
    }
    return render(request, 'home/home.html', context)

