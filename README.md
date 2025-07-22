# 🌦️ AlertaClima

Aplicación CLI en Python que permite consultar el clima actual de cualquier ciudad usando la API gratuita de WeatherAPI.com. Además, guarda un historial básico de consultas durante la sesión.

---

## 🚀 Funcionalidades

- Consulta del clima actual por ciudad.
- Integración con la API de WeatherAPI.com.
- Lectura segura de la clave API desde un archivo `.env`.
- Manejo de errores y mensajes claros al usuario.
- Menú interactivo en línea de comandos.
- Historial en memoria de consultas realizadas durante la sesión.

---

## 🧰 Tecnologías usadas

- Python 3.11
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- API de [WeatherAPI.com](https://www.weatherapi.com/)

---

## ⚙️ Cómo usarlo

1. Clonar el repositorio:

```bash
git clone https://github.com/harikirtandas/alerta-clima.git
cd alerta-clima
```

2. Activar un entorno virtual y luego instalar dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Crear un archivo `.env` en la raíz del proyecto y agregar la API Key de WeatherAPI:

```
WEATHERAPI_KEY=tu_clave_api_aqui
```

4. Ejecutar el script principal:

```bash
python main.py
```

---

## 📁 Estructura del proyecto

```plaintext
alerta-clima/
├── main.py                 # Menú principal CLI
├── clima_api.py            # Funciones para consultar clima usando WeatherAPI
├── .env                    # (oculto) Clave API WeatherAPI
├── .gitignore              # Evita subir archivos sensibles
├── data/                   # Carpeta para futuros archivos (historial, logs)
```

---

## 📝 Estado actual del proyecto

✅ Consulta de clima por ciudad con WeatherAPI  
✅ Menú interactivo en consola  
✅ Historial básico en memoria  
🔜 Guardado persistente de historial  
🔜 Funcionalidad de alertas meteorológicas (en desarrollo)

---

## 📌 Autor

Desarrollado por [Jor](https://github.com/harikirtandas/alerta-clima)  
Proyecto en proceso de evolución como parte de mi camino para trabajar como Python Developer.

---

## 🧠 Licencia

MIT
