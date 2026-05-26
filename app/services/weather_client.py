# ==========================================
# Weather API Client
# Cliente para consumir la API de Open-Meteo
# ==========================================

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT = 10


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
        response = requests.get(
            GEOCODING_URL,
            params=params,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            return None

        city = data["results"][0]

        return {
            "name": city.get("name"),
            "country": city.get("country"),
            "latitude": city.get("latitude"),
            "longitude": city.get("longitude"),
        }

    except requests.exceptions.RequestException:
        return None
    except ValueError:
        return None
    except KeyError:
        return None


def get_current_weather(latitude, longitude):
    """
    Obtiene el clima actual usando latitud y longitud.
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
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        data = response.json()

        if "current" not in data:
            return None

        current = data["current"]

        return {
            "temperature_2m": current.get("temperature_2m"),
            "relative_humidity_2m": current.get("relative_humidity_2m"),
            "weather_code": current.get("weather_code"),
        }

    except requests.exceptions.RequestException:
        return None
    except ValueError:
        return None
    except KeyError:
        return None


def get_weather_forecast(latitude, longitude):
    """
    Consulta el pronóstico básico de los próximos días.
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
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()

        data = response.json()

        if "daily" not in data:
            return None

        daily = data["daily"]

        required_keys = [
            "time",
            "temperature_2m_max",
            "temperature_2m_min",
            "weather_code",
        ]

        for key in required_keys:
            if key not in daily:
                return None

        return daily

    except requests.exceptions.RequestException:
        return None
    except ValueError:
        return None
    except KeyError:
        return None