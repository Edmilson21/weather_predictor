# 🌤️ Weather Predictor API

API REST para predecir la temperatura basada en datos climáticos, construida con Django REST Framework y Machine Learning.

## Demo en vivo
[https://weather-predictor-p8qp.onrender.com/weather/](https://weather-predictor-p8qp.onrender.com/weather/)

## Interfaz
<img width="867" height="878" alt="Captura de pantalla (228)" src="https://github.com/user-attachments/assets/09e9bae7-5c12-48d8-9d16-778ef18038c4" />
<hr>
## Tecnologías
- Python 3.11
- Django REST Framework
- scikit-learn (Random Forest Regressor)
- Docker
- Render (deploy)

## Dataset
Weather History Dataset — 96.453 registros, variables climáticas como humedad, viento, presión y visibilidad.

## Rendimiento del modelo
- **MAE:** 2.18°C
- **R²:** 0.91

## Cómo usar la API

**Endpoint:** `POST /weather/predecir/`

**Body JSON:**
```json
{
    "humedad": 0.89,
    "velocidad_viento": 14.1,
    "wind_bearing": 251,
    "visibilidad": 15.8,
    "presion": 1015.13,
    "mes": 1,
    "hora": 9
}
```

**Respuesta:**
```json
{
    "temperatura": 5.94
}
```

## Instalación local

```bash
git clone https://github.com/Edmilson21/weather_predictor
cd weather-predictor
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Con Docker

```bash
docker build -t weather-api .
docker run -p 8000:8000 weather-api
```
