import requests
from django.http import JsonResponse
from django.shortcuts import render

BASE_URL = "https://hackeps-poke-backend.azurewebsites.net"


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


def zone_post(request, endpoint, zone_id):
    api_url = f"{BASE_URL}/{endpoint}/{zone_id}"

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
