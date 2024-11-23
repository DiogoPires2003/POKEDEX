import requests

API_URL = "https://hackeps-poke-backend.azurewebsites.net/docs#/"


def fetch_pokemon_data():
    """
    Obtiene la lista de Pokémon desde la API externa.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lanza un error si el request falla
        return response.json()  # Devuelve los datos en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API: {e}")
        return []  # Devuelve una lista vacía en caso de error
