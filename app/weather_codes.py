# ==========================================
# Weather API Client
# Conversión de códigos del clima
# ==========================================


def get_weather_description(weather_code):
    """
    Convierte un código de clima de Open-Meteo
    en una descripción entendible para el usuario.
    """

    # Diccionario basado en códigos comunes de Open-Meteo
    weather_codes = {
        0: "Cielo despejado",
        1: "Principalmente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia intensa",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos fuertes",
        95: "Tormenta eléctrica",
    }

    # Si el código no existe en el diccionario,
    # regresamos un mensaje genérico.
    return weather_codes.get(weather_code, "Descripción no disponible")