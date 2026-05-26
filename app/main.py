# ==========================================
# Weather API Client
# Archivo principal de ejecución
# ==========================================

from weather_client import get_city_coordinates, get_current_weather


def main():
    """
    Función principal del programa.
    """

    print("===================================")
    print(" Weather API Client")
    print("===================================")

    # Ciudad de prueba
    city_name = "Pachuca"

    # Buscamos coordenadas de la ciudad
    city = get_city_coordinates(city_name)

    # Validamos si la ciudad fue encontrada
    if city is None:
        print("No se encontró la ciudad.")
        return

    # Consultamos el clima actual usando coordenadas
    weather = get_current_weather(city["latitude"], city["longitude"])

    print()
    print(f"Ciudad: {city['name']}, {city['country']}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Humedad: {weather['relative_humidity_2m']} %")
    print(f"Código del clima: {weather['weather_code']}")


if __name__ == "__main__":
    main()