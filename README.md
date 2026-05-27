# Weather API Client

Aplicación desarrollada en Python para consultar información del clima utilizando la API pública de Open-Meteo.

El proyecto fue construido paso a paso con enfoque educativo y profesional, aplicando buenas prácticas de estructura, modularización, consumo de APIs REST, manejo de JSON, validaciones, testing automatizado y control de versiones con Git y GitHub.

---

# Características

- Consulta de clima por ciudad
- Obtención de temperatura actual
- Obtención de humedad
- Descripción amigable del clima
- Pronóstico básico de 3 días
- Validación de entradas del usuario
- Manejo de errores HTTP y respuestas inválidas
- Testing automatizado con pytest
- Estructura modular profesional
- Workflow Git con ramas `main` y `dev`

---

# Tecnologías utilizadas

- Python 3
- Requests
- Pytest
- Open-Meteo API
- Git
- GitHub

---

# Estructura del proyecto

```text
weather-api-client/
│
├── app/
│   ├── services/
│   │   ├── __init__.py
│   │   └── weather_client.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── display.py
│   │   └── validators.py
│   │
│   ├── __init__.py
│   ├── main.py
│   └── weather_codes.py
│
├── tests/
│   └── test_weather_codes.py
│
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/AlfredoVelazquez/weather-api-client.git
```

## 2. Entrar al proyecto

```bash
cd weather-api-client
```

## 3. Crear entorno virtual

```bash
python -m venv venv
```

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

Desde la raíz del proyecto:

```bash
python app/main.py
```

---

# Ejemplo de uso

```text
===================================
 Weather API Client
===================================

Ingresa una ciudad: Guadalajara

========= CLIMA ACTUAL =========
Ciudad: Guadalajara, México
Temperatura: 34.1 °C
Humedad: 13 %
Clima: Parcialmente nublado

========= PRONÓSTICO =========

Fecha: 2026-05-26
Temperatura máxima: 34.3 °C
Temperatura mínima: 19.2 °C
Clima: Nublado
```

---

# Testing

Ejecutar pruebas automatizadas:

```bash
pytest
```

Resultado esperado:

```text
4 passed
```

---

# Conceptos practicados

- APIs REST
- Peticiones HTTP con Requests
- Manejo de JSON
- Validaciones
- Manejo de errores
- Modularización
- Testing automatizado
- Git y GitHub
- Buenas prácticas en Python

---

# Flujo Git utilizado

- `main` → rama estable
- `dev` → desarrollo y pruebas

---

# API utilizada

Open-Meteo:

https://open-meteo.com/

---

# Autor

José Alfredo Velázquez León