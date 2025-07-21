# 🌦️ AlertaClima

Una app de línea de comandos desarrollada en Python que permite consultar las coordenadas geográficas de una ciudad ingresada por el usuario, con el objetivo de mostrar posibles alertas climáticas de la zona (en desarrollo).

---

## 🚀 Funcionalidades

- Consulta de coordenadas (latitud y longitud) a partir del nombre de una ciudad.
- Integración con la API de OpenWeatherMap.
- Lectura segura de claves API desde un archivo `.env`.
- Manejo de errores y mensajes claros al usuario.
- Estructura modular y lista para escalar.
- **[En desarrollo]**: Consulta de alertas meteorológicas.

---

## 🧰 Tecnologías usadas

- Python 3.11
- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- API de [OpenWeatherMap](https://openweathermap.org/api)

---

## ⚙️ Cómo usarlo

1. Cloná el repositorio:

```bash
git clone https://github.com/harikirtandas/alerta-clima.git
cd alerta-clima
```

2. Activá un entorno virtual y instalá dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Creá un archivo .env en la raíz del proyecto y agregá tu API Key:

```bash
API_KEY=tu_clave_de_openweathermap
```

4. Ejecutá el script:

```bash
python main.py
```

---

## 📁 Estructura del proyecto

```plaintext
alerta-clima/
├── main.py                 # Menú principal CLI
├── clima_api.py            # Funciones para consultar coordenadas y alertas
├── .env                    # (oculto) Clave de API
├── .gitignore              # Evita subir archivos sensibles
├── data/
│   └── historial_alertas.json  # Archivo para almacenar alertas (próximamente)
```

---

## 📝 Estado actual del proyecto

✅ Módulo de geolocalización por ciudad  
✅ Integración básica con API  
❌ Alertas climáticas activas (en pausa por requerir suscripción adicional)  
🔜 Historial de consultas y filtros por fecha/ciudad

---

## 📌 Autor

Desarrollado por [Jor](https://github.com/harikirtandas/alerta-clima)  
Proyecto en proceso de evolución como parte de mi camino para trabajar como Python Developer.

---

## 🧠 Licencia

MIT

---
