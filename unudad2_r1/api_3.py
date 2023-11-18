import requests

url = "https://api.tomorrow.io/v4/weather/forecast"
api_key = "wWHwADySE1tOvEWdoS0c0ZfVZxAX0U9k"

def obtener_pronostico(tiempo_api_key):
    latitud = input("Ingresa la latitud: ")
    longitud = input("Ingresa la longitud: ")

    parametros = {
        "location": f"{latitud},{longitud}",
        "apikey": tiempo_api_key,
    }

    try:
        response = requests.get(url, params=parametros)
        response.raise_for_status()  # Esto lanzará una excepción si hay un error HTTP

        data = response.json()
        # Trabaja con los datos obtenidos
        print("Información del pronóstico del tiempo:")
        print(data)

    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Error de tiempo de espera: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error no identificado: {err}")

# Llamada a la función de ejemplo
obtener_pronostico(api_key)