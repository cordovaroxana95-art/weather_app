from fastapi import APIRouter, HTTPException
from app.services.geolocation_service import get_coordinates
from app.services.weather_service import get_weather
from app.utils.validation import sanitize_city

router = APIRouter(prefix="/weather", tags=["Weather"])

@router.get("/")
async def get_weather_by_city(city: str):
    city = sanitize_city(city)
    if not city:
        raise HTTPException(status_code=400, detail="Ciudad inválida o vacía")

    coords = await get_coordinates(city)
    if coords is None:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    weather_data = await get_weather(coords)
    if weather_data is None:
        raise HTTPException(status_code=500, detail="Error al obtener el clima")

    return weather_data