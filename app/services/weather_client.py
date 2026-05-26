# ==========================================
# Weather API Client
# Cliente para consumir la API de Open-Meteo
# ==========================================

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city_name):
    """
    Busca una ciudad y obtiene sus coordenadas.
    """

    params = {
        "name": city_name,
        "count": 1,
        "language": "es",
        "format": "json",
    }

    try:
        # Timeout evita que el programa se quede esperando indefinidamente.
        response = requests.get(GEOCODING_URL, params=params, timeout=10)

        # Lanza un error si la API responde con 4xx o 5xx.
        response.raise_for_status()

        data = response.json()

        if "results" not in data:
            return None

        city = data["results"][0]

        return {
            "name": city["name"],
            "country": city["country"],
            "latitude": city["latitude"],
            "longitude": city["longitude"],
        }

    except requests.exceptions.RequestException:
        print("Error: no se pudo conectar con la API de ciudades.")
        return None


def get_current_weather(latitude, longitude):
    """
    Consulta el clima actual usando latitud y longitud.
    """

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,weather_code",
        "timezone": "auto",
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "current" not in data:
            return None

        return data["current"]

    except requests.exceptions.RequestException:
        print("Error: no se pudo consultar el clima actual.")
        return None