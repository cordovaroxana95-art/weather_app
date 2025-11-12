# 🌦️ WeatherApp Secure — Aplicación Global del Clima

WeatherApp Secure es una aplicación moderna y segura que permite consultar el clima actual de **cualquier ciudad del mundo** 🌍.  
Utiliza la API **Open-Meteo** junto con **OpenStreetMap (Nominatim)** para obtener coordenadas precisas y mostrar datos meteorológicos en tiempo real.

---

## 🧱 Estructura del Proyecto
weather_app/
│
├── backend/ # API con FastAPI (segura y optimizada)
│ ├── app/
│ │ ├── api/ # Endpoints
│ │ ├── core/ # Configuración y excepciones
│ │ ├── middleware/ # Protección y limitación de solicitudes
│ │ ├── services/ # Comunicación con APIs externas
│ │ ├── utils/ # Validación de entradas
│ │ └── main.py # Punto de entrada del servidor
│ ├── .env # Variables de entorno (configuración segura)
│ └── requirements.txt # Dependencias de Python
│
├── frontend/ # Interfaz React + Tailwind
│ ├── src/
│ │ ├── components/
│ │ │ └── WeatherApp.jsx
│ │ ├── App.jsx
│ │ └── main.jsx
│ ├── index.html
│ └── package.json
│
└── README.md
## 🚀 Características Principales

✅ **Clima Global** — Consulta cualquier ciudad del mundo  
✅ **Diseño Moderno** — UI minimalista con TailwindCSS  
✅ **Backend Seguro** — API con FastAPI, validación y rate limiting  
✅ **Código Limpio y Escalable** — Separación por capas y buenas prácticas  
✅ **Manejo de Errores Inteligente** — Feedback claro y controlado  
✅ **Configuración Simple** — Rápida instalación y despliegue

---

## 🧰 Tecnologías Utilizadas

**Backend:**
- 🐍 [FastAPI](https://fastapi.tiangolo.com/)
- 🌐 [HTTPX](https://www.python-httpx.org/)
- ⚙️ Python 3.10+
- 🔐 Rate limiting y validación de entrada

**Frontend:**
- ⚛️ [React](https://react.dev/)
- 🎨 [TailwindCSS](https://tailwindcss.com/)
- ⚡ [Vite](https://vitejs.dev/) (compilador rápido)

**APIs Externas:**
- 🗺️ [Nominatim OpenStreetMap](https://nominatim.org/) — para geocodificación  
- 🌤️ [Open-Meteo](https://open-meteo.com/) — para datos meteorológicos  

---

## ⚙️ Instalación y Configuración

### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/tuusuario/weather_app_secure.git
cd weather_app

2️⃣ Backend — FastAPI
Instala dependencias
cd backend
pip install -r requirements.txt

Ejecuta el servidor
uvicorn app.main:app --reload

Por defecto, el backend se ejecuta en:
👉 http://localhost:8000

3️⃣ Frontend — React
Instala dependencias

cd frontend
npm install

Ejecuta el servidor de desarrollo
npm run dev

Por defecto, el frontend se ejecuta en:
👉 http://localhost:5173

🔑 Configuración de API y Autenticación

⚠️ Open-Meteo y Nominatim no requieren clave API, por lo que no necesitas credenciales.
Si en el futuro integras otro servicio (por ejemplo, OpenWeatherMap), deberás añadir tu API Key en el archivo .env:
API_KEY=tu_clave_aqui

Y acceder a ella desde el backend con:
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

🧩 Uso

Escribe el nombre de una ciudad (ej. Tokyo, Madrid, Ciudad de México).

Presiona “Buscar Clima”.

Visualiza:

🌡️ Temperatura en °C y °F

💨 Velocidad del viento

☁️ Código de clima

Si la ciudad no existe, se mostrará un mensaje claro de error.

🔐 Seguridad y Buenas Prácticas
| Mecanismo                           |       Descripción                                     |
| ----------------------------------- | ----------------------------------------------------- |
| **Validación de entradas**          | Evita inyecciones o valores maliciosos                |
| **Rate Limiting**                   | Bloquea ataques de denegación de servicio (DoS)       |
| **CORS restringido**                | Solo permite solicitudes desde el frontend autorizado |
| **Timeouts seguros**                | Evita bloqueos prolongados en peticiones externas     |
| **Manejo centralizado de errores**  | Mejora la estabilidad y la trazabilidad               |
| **Separación de responsabilidades** | Backend modular y mantenible                          |

🧪 Manejo de Errores Comunes

| Error                             | Causa                                         | Solución                                    |
| --------------------------------- | --------------------------------------------- | ------------------------------------------- |
| ❌ *400 Ciudad inválida*           | Entrada vacía o no permitida                  | Verifica que el nombre no contenga símbolos |
| ❌ *404 Ciudad no encontrada*      | API de geolocalización no encontró resultados | Intenta con una ciudad reconocida           |
| ❌ *500 Error al obtener el clima* | Fallo de red o API externa                    | Espera e inténtalo de nuevo                 |
| ❌ *429 Demasiadas solicitudes*    | Límite de peticiones alcanzado                | Espera 1 minuto antes de reintentar         |


🧱 Arquitectura y Flujo de Datos

🧑 Usuario
   ↓
[Frontend React]
   ↓ (GET /weather?city=Tokyo)
[FastAPI Backend]
   ├── Validación (sanitize_city)
   ├── Geolocalización (Nominatim)
   ├── Clima (Open-Meteo)
   ↓
💾 Respuesta JSON estructurada
   ↓
[Frontend muestra los resultados]

🧩 Scripts Útiles
| Comando                         | Descripción                           |
| ------------------------------- | ------------------------------------- |
| `npm run dev`                   | Inicia el frontend en modo desarrollo |
| `uvicorn app.main:app --reload` | Inicia el backend                     |
| `npm run build`                 | Compila el frontend para producción   |
| `pip freeze > requirements.txt` | Actualiza dependencias Python         |


💬 Contribuciones

¡Las contribuciones son bienvenidas!
Por favor, abre un Pull Request o Issue con tus mejoras o sugerencias.

📜 Licencia

Este proyecto se distribuye bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente, dando crédito al autor original.

✨ Autor

Desarrollado por Roxana Córdova con ❤️ y pasión por la ciberseguridad y el desarrollo limpio.
🔒 Código seguro. 🧠 Código claro. 🌎 Clima global.
