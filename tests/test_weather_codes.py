# ==========================================
# Weather API Client
# Pruebas unitarias para weather_codes.py
# ==========================================

# Importamos la función que vamos a probar
from app.weather_codes import get_weather_description


def test_clear_sky():
    """
    Verifica que el código 0
    regrese 'Cielo despejado'.
    """

    assert get_weather_description(0) == "Cielo despejado"


def test_cloudy_weather():
    """
    Verifica descripción de clima nublado.
    """

    assert get_weather_description(3) == "Nublado"


def test_thunderstorm_weather():
    """
    Verifica descripción de tormenta eléctrica.
    """

    assert get_weather_description(95) == "Tormenta eléctrica"


def test_unknown_weather_code():
    """
    Verifica códigos inexistentes.
    """

    assert (
        get_weather_description(999)
        == "Descripción no disponible"
    )