import requests
from django.http import JsonResponse


def obtener_pokemons(request):
    url = "https://hackeps-poke-backend.azurewebsites.net/pokemon"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Asegura que la respuesta sea 200
        data = response.json()  # Convierte la respuesta a JSON
        return JsonResponse(data, safe=False)  # Devuelve la respuesta como JSON
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Error al conectar con la API: {str(e)}"}, status=500)


def detalle_pokemon(request, pokemon_id):
    url = f"https://hackeps-poke-backend.azurewebsites.net/pokemon/{pokemon_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Error al obtener el Pokémon: {str(e)}"}, status=500)

def info_team(request):
    url=f"https://hackeps-poke-backend.azurewebsites.net/teams/8c4d959b-64bb-4952-9f23-b0f76d93c733"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Error al obtener el InfoTeam: {str(e)}"}, status=500)

