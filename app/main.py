# ==========================================
# Weather API Client
# Archivo principal de ejecución
# ==========================================

from services.weather_client import (
    get_city_coordinates,
    get_current_weather,
    get_weather_forecast,
)
from utils.display import (
    show_header,
    show_weather_result,
    show_forecast_result,
    show_error,
)
from utils.validators import validate_city_name
from weather_codes import get_weather_description


def main():
    """
    Función principal del programa.
    Coordina el flujo general de la aplicación.
    """

    # Mostramos el encabezado principal
    show_header()

    # Pedimos al usuario la ciudad
    city_input = input("Ingresa una ciudad: ")

    # Validamos que la ciudad no esté vacía
    city_name = validate_city_name(city_input)

    if city_name is None:
        show_error("debes ingresar una ciudad.")
        return

    # Obtenemos las coordenadas de la ciudad
    city = get_city_coordinates(city_name)

    if city is None:
        show_error("no se encontró información de la ciudad.")
        return

    # Consultamos el clima actual
    weather = get_current_weather(
        city["latitude"],
        city["longitude"]
    )

    if weather is None:
        show_error("no se pudo obtener el clima actual.")
        return

    # Convertimos el código del clima actual a descripción
    current_description = get_weather_description(
        weather["weather_code"]
    )

    # Mostramos el clima actual
    show_weather_result(
        city,
        weather,
        current_description
    )

    # Consultamos el pronóstico básico
    forecast = get_weather_forecast(
        city["latitude"],
        city["longitude"]
    )

    if forecast is None:
        show_error("no se pudo obtener el pronóstico.")
        return

    # Mostramos el pronóstico de próximos días
    show_forecast_result(
        forecast,
        get_weather_description
    )


if __name__ == "__main__":
    main()