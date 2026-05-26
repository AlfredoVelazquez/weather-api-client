# ==========================================
# Weather API Client
# Introducción a requests y JSON
# ==========================================

# Importamos la librería requests
# Esta librería permite hacer peticiones HTTP
import requests


# Función principal del programa
def main():

    # URL de prueba para aprender requests
    url = "https://jsonplaceholder.typicode.com/users/1"

    print("Realizando petición HTTP...")
    print()

    # Realizamos una petición GET
    response = requests.get(url)

    # Mostramos el código de estado HTTP
    print(f"Código de estado: {response.status_code}")
    print()

    # Convertimos la respuesta JSON
    # en un diccionario de Python
    data = response.json()

    # Mostramos información específica
    print("Datos recibidos:")
    print(f"Nombre: {data['name']}")
    print(f"Usuario: {data['username']}")
    print(f"Correo: {data['email']}")


# Punto de entrada principal
if __name__ == "__main__":
    main()