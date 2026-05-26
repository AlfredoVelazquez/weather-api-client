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

    # Parámetros enviados a la API
    params = {
        "name": city_name,
        "count": 1,
        "language": "es",
        "format": "json",
    }

    try:

        # Realizamos petición HTTP GET
        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=10
        )

        # Verificamos errores HTTP
        response.raise_for_status()

        # Convertimos JSON a diccionario Python
        data = response.json()

        # Validamos si hubo resultados
        if "results" not in data:
            return None

        # Tomamos la primera ciudad encontrada
        city = data["results"][0]

        return {
            "name": city["name"],
            "country": city["country"],
            "latitude": city["latitude"],
            "longitude": city["longitude"],
        }

    except requests.exceptions.RequestException:

        print("Error: no se pudo conectar con la API.")
        return None


def get_current_weather(latitude, longitude):
    """
    Obtiene el clima actual.
    """

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "weather_code"
        ),
        "timezone": "auto",
    }

    try:

        response = requests.get(
            WEATHER_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Validamos existencia de datos
        if "current" not in data:
            return None

        return data["current"]

    except requests.exceptions.RequestException:

        print("Error: no se pudo consultar el clima actual.")
        return None


def get_weather_forecast(latitude, longitude):
    """
    Consulta el pronóstico básico
    de los próximos días.
    """

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "weather_code"
        ),
        "timezone": "auto",
        "forecast_days": 3,
    }

    try:

        response = requests.get(
            WEATHER_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Validamos que exista la sección daily
        if "daily" not in data:
            return None

        return data["daily"]

    except requests.exceptions.RequestException:

        print("Error: no se pudo consultar el pronóstico.")
        return None