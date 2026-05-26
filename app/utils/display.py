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
    Muestra el resultado del clima actual.
    """

    print()
    print("========= CLIMA ACTUAL =========")
    print(f"Ciudad: {city['name']}, {city['country']}")
    print(f"Temperatura: {weather['temperature_2m']} °C")
    print(f"Humedad: {weather['relative_humidity_2m']} %")
    print(f"Clima: {description}")


def show_forecast_result(forecast, get_description_function):
    """
    Muestra el pronóstico básico de los próximos días.
    """

    print()
    print("========= PRONÓSTICO =========")

    # Extraemos listas del diccionario forecast
    dates = forecast["time"]
    max_temperatures = forecast["temperature_2m_max"]
    min_temperatures = forecast["temperature_2m_min"]
    weather_codes = forecast["weather_code"]

    # Recorremos cada día del pronóstico
    for index in range(len(dates)):

        # Convertimos el weather_code en texto amigable
        description = get_description_function(
            weather_codes[index]
        )

        print()
        print(f"Fecha: {dates[index]}")
        print(f"Temperatura máxima: {max_temperatures[index]} °C")
        print(f"Temperatura mínima: {min_temperatures[index]} °C")
        print(f"Clima: {description}")


def show_error(message):
    """
    Muestra mensajes de error.
    """

    print()
    print(f"Error: {message}")