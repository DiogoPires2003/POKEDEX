import requests
from django.shortcuts import render


# Create your views here.
def home(request):
    # URL del endpoint para el equipo
    team_id = "8c4d959b-64bb-4952-9f23-b0f76d93c733"
    api_url = f"https://hackeps-poke-backend.azurewebsites.net/teams/{team_id}"

    try:
        # Hacer la solicitud GET a la API
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción para errores HTTP
        team_data = response.json()  # Decodifica el JSON
        captured_pokemons = team_data.get("captured_pokemons", [])


    except requests.exceptions.RequestException as e:
        # Manejar errores
        print(f"Error al conectar con la API: {e}")
        captured_pokemons = []

    # Pasar la lista de Pokémon capturados al contexto
    context = {
        "captured_pokemons": captured_pokemons
    }
    return render(request, 'home/home.html', context)

def pokemon_names(request, id):
    api_url = f"https://hackeps-poke-backend.azurewebsites.net/pokemons/{id}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción para errores HTTP
        pokemon_data = response.json()  # Decodifica el JSON
        pokemon_name = pokemon_data.get("name")

    except requests.exceptions.RequestException as e:
        # Manejar errores
        print(f"Error al conectar con la API: {e}")
        pokemon_name

    context = {
        "pokemon_name": pokemon_name
    }
    return render(request,'home/pokemonName.html',context)