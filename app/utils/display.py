# ==========================================
# Weather API Client
# Funciones para mostrar información en consola
# ==========================================


def show_header():
    """
    Muestra el encabezado principal del programa.
    """

    print("===================================")
    print(" Weather API Client")
    print("===================================")
    print()


def show_weather_result(city, weather, description):
    """
    Muestra el resultado del clima en consola.
    """

    print()
    print("========= RESULTADO =========")
    print(f"Ciudad: {city['name']}, {city['country']}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Humedad: {weather['relative_humidity_2m']} %")
    print(f"Clima: {description}")


def show_error(message):
    """
    Muestra mensajes de error de forma uniforme.
    """

    print()
    print(f"Error: {message}")