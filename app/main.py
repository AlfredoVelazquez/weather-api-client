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
    print()

    # Solicitamos al usuario el nombre de una ciudad
    city_name = input("Ingresa una ciudad: ")

    # Eliminamos espacios innecesarios
    city_name = city_name.strip()

    # Validamos que el usuario haya escrito algo
    if city_name == "":
        print()
        print("Error: debes ingresar una ciudad.")
        return

    # Buscamos información de la ciudad
    city = get_city_coordinates(city_name)

    # Validamos si la ciudad existe
    if city is None:
        print()
        print("No se encontró información de la ciudad.")
        return

    # Consultamos el clima actual
    weather = get_current_weather(
        city["latitude"],
        city["longitude"]
    )

    # Validamos si el clima fue obtenido correctamente
    if weather is None:
        print()
        print("No se pudo obtener el clima actual.")
        return

    # Convertimos el código del clima
    # en una descripción amigable
    description = get_weather_description(
        weather["weather_code"]
    )

    print()
    print("========= RESULTADO =========")
    print(f"Ciudad: {city['name']}, {city['country']}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Humedad: {weather['relative_humidity_2m']} %")
    print(f"Clima: {description}")


# Punto de entrada principal
if __name__ == "__main__":
    main()