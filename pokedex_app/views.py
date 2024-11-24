import requests
from django.http import JsonResponse
from django.shortcuts import render
import random

BASE_URL = "https://hackeps-poke-backend.azurewebsites.net"

team_id = "8c4d959b-64bb-4952-9f23-b0f76d93c733"
# Create your views here.
def home(request):

    # URL del endpoint para el equipo
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


def proxy_api(request, endpoint):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    response.raise_for_status()
    return JsonResponse(response.json(), safe=False)


def team_detail(request, endpoint, team_id):
    api_url = f"{BASE_URL}/{endpoint}/{team_id}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Maneja errores HTTP
        team_data = response.json()  # Convierte la respuesta a JSON
    except requests.exceptions.RequestException as e:
        # Devuelve un error en caso de fallo
        return JsonResponse({"error": f"Error connecting to API: {str(e)}"}, status=500)

    # Devuelve los datos del equipo como JSON
    return JsonResponse(team_data, safe=False)



def zone_post(request):
    if request.method == "POST":
        zone_id = request.POST.get("zone_id")
        zone_id_from_form = request.POST.get("zone_id", zone_id)

        api_url = f"{BASE_URL}/events/{zone_id}"

    if request.method == "POST":
        try:
            payload = request.POST.dict()

            payload['team_id'] = '8c4d959b-64bb-4952-9f23-b0f76d93c733'

            headers = {"Content-Type": "application/json"}

            response = requests.post(api_url, json=payload, headers=headers)
            response.raise_for_status()

            response_data = response.json()
        except requests.exceptions.RequestException as e:
            # Manejar errores si la conexión falla
            return JsonResponse({"error": f"Error al conectar con la API: {str(e)}"}, status=500)

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Método no permitido, solo POST es soportado."}, status=405)

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

def list_Pokemons(request):

    api_url = f"{BASE_URL}/pokemons"

    api_pokemons_obtained = f"{BASE_URL}/teams/{team_id}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza excepción para errores HTTP
        pokemons_data = response.json()  # Decodifica el JSON
        pokemons_response = requests.get(api_pokemons_obtained)
        pokemons_response.raise_for_status()
        pokemons_obtained = pokemons_response.json()
        pokemonsId = [pokemon['pokemon_id'] for pokemon in pokemons_obtained.get("captured_pokemons", [])]



    except requests.exceptions.RequestException as e:
        # Manejar errores
        print(f"Error al conectar con la API: {e}")

    context = {
        "pokemons": pokemons_data,
        "captured_pokemons": pokemonsId
    }

    return render(request, 'Pokedex.html', context)


def zone_get(request, zone_id):
    api_url = f"{BASE_URL}/zones/{zone_id}"  # URL externa

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        zone_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return JsonResponse({"error": "No se pudo obtener la información de la zona"}, status=500)

    return JsonResponse(zone_data)


def tournament_get(request, tournament_id):
    api_url = f"{BASE_URL}/tournaments/{tournament_id}"  # URL externa

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        zone_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return JsonResponse({"error": "No se pudo obtener la información de la zona"}, status=500)

    return JsonResponse(zone_data)


def pokemon_get(request, pokemon_id):
    api_url = f"{BASE_URL}/pokemons/{pokemon_id}"  # URL externa

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        zone_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return JsonResponse({"error": "No se pudo obtener la información de la zona"}, status=500)

    return JsonResponse(zone_data)


def detail(request,id):
    return render(request, 'home/info.html')

def whoIsThatPokemon(request):
    random_id = random.randint(1,153)
    api_url = f"{BASE_URL}/pokemons/{random_id}"

    respons = requests.get(api_url)
    respons.raise_for_status()
    pokemon = respons.json()
    context={
        "pokemon": pokemon
    }

    return render(request, 'whoIsThatPokemon.html', context)
