from dotenv import load_dotenv
import os
import requests # Permite hacer peticiones HTTP a la API de OpenWeatherMap.

load_dotenv()  # Carga las variables del archivo .env

api_key = os.getenv("API_KEY")
print(f"API Key cargada: {api_key}")

def coordenadas(ciudad):
    # url es un dato str
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=1&appid={api_key}'
    
    # Hacemos la consulta HTTP
    consulta = requests.get(url) # Es el objeto Response

    # verificación del código de estado (status_code)
    if consulta.status_code == 200:
        # Usamos .json() para obtener los datos.
        # print(consulta.json()) # línea de verificación
        data = consulta.json()
        
        if not data:
            print('Error. Verifique el nombre de la ciudad')
            return None
        else:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return {"lat": lat, "lon": lon}
    else:
        print("Error al consultar la API. Código:", consulta.status_code)
    
    

# print(coordenadas('Madrid')) # línea de verificación

# Creamos la función para consultar alertas 
def alertas_climaticas(lat, lon):
    url_alerta = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,current&appid={api_key}&lang=es'
    consulta_alerta = requests.get(url_alerta) # Hacemos la consulta 
    # verificación del código de estado (status_code)
    if consulta_alerta.status_code == 200:
        alerta = consulta_alerta.json()
        if not alerta:
            print('No hay alertas en tu ciudad')
        else:
            return alerta
    else:
        print("Error al consultar la API. Código:", consulta_alerta.status_code)

loc = coordenadas('Madrid')
if loc:
    alertas = alertas_climaticas(loc['lat'], loc['lon'])
    print(alertas)  # para ver qué devuelve  
    
def test_api_key(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print(response.json())
    
test_api_key(-34.6037, -58.3816)  # Buenos Aires