# ==========================================
# Weather API Client
# Cliente para consumir la API de Open-Meteo
# ==========================================

import requests


# URL base para buscar ciudades
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

# URL base para consultar el clima
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city_name):
    """
    Busca una ciudad y obtiene sus coordenadas.
    """

    # Parámetros que se enviarán a la API de geocoding
    params = {
        "name": city_name,
        "count": 1,
        "language": "es",
        "format": "json"
    }

    # Realizamos una petición GET a la API
    response = requests.get(GEOCODING_URL, params=params)

    # Convertimos la respuesta JSON en diccionario de Python
    data = response.json()

    # Validamos si la API encontró resultados
    if "results" not in data:
        return None

    # Tomamos el primer resultado encontrado
    city = data["results"][0]

    return {
        "name": city["name"],
        "country": city["country"],
        "latitude": city["latitude"],
        "longitude": city["longitude"]
    }


def get_current_weather(latitude, longitude):
    """
    Consulta el clima actual usando latitud y longitud.
    """

    # Parámetros enviados a la API del clima
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code",
        "timezone": "auto"
    }

    # Realizamos la petición GET
    response = requests.get(WEATHER_URL, params=params)

    # Convertimos la respuesta JSON a diccionario
    data = response.json()

    # Retornamos únicamente la sección de clima actual
    return data["current"]