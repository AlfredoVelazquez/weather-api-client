# ==========================================
# Weather API Client
# Validaciones generales del proyecto
# ==========================================


def validate_city_name(city_name):
    """
    Valida que el nombre de la ciudad no esté vacío.
    """

    # Eliminamos espacios al inicio y al final
    city_name = city_name.strip()

    # Si después de limpiar el texto queda vacío,
    # la ciudad no es válida.
    if city_name == "":
        return None

    return city_name