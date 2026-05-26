# ==========================================
# Weather API Client
# Archivo principal de ejecución
# ==========================================

from weather_client import get_city_coordinates, get_current_weather
from weather_codes import get_weather_description


def main():
    """
    Función principal del programa.
    """

    print("===================================")
    print(" Weather API Client")
    print("===================================")

    city_name = "Pachuca"

    city = get_city_coordinates(city_name)

    if city is None:
        print("No se encontró información de la ciudad.")
        return

    weather = get_current_weather(city["latitude"], city["longitude"])

    if weather is None:
        print("No se pudo obtener el clima actual.")
        return

    description = get_weather_description(weather["weather_code"])

    print()
    print(f"Ciudad: {city['name']}, {city['country']}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Humedad: {weather['relative_humidity_2m']} %")
    print(f"Clima: {description}")


if __name__ == "__main__":
    main()