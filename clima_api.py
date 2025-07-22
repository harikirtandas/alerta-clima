from dotenv import load_dotenv # importa la función para cargar variables de entorno desde un archivo .env
import os # acceder a las variables de entorno
import requests # Permite hacer peticiones HTTP a la API de OpenWeatherMap.

load_dotenv()  # Carga las variables del archivo .env

# Función para integrar WeatherAPI
def clima_actual_weatherapi(ciudad):
    weatherapi_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={ciudad}&aqi=no"

    try:
        response = requests.get(url)
        data = response.json()
        # print(weatherapi_key) # línea de verificación
        if "error" in data:
            return f"⚠️ Error: {data['error']['message']}"

        ciudad = data['location']['name']
        region = data['location']['region']
        pais = data['location']['country']
        temp = data['current']['temp_c']
        condicion = data['current']['condition']['text']

        return f"📍 {ciudad}, {region}, {pais} | 🌡 {temp}°C | 🌥 {condicion}"

    except Exception as e:
        return f"❌ Error al conectar con WeatherAPI: {e}"
    
    