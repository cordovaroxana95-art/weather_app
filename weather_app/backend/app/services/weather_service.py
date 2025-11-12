import httpx

async def get_weather(coords):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current_weather": True,
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    cw = data.get("current_weather")
    if not cw:
        return None

    return {
        "city": f"Lat: {coords['lat']} Lon: {coords['lon']}",
        "temp_c": cw.get("temperature"),
        "temp_f": round((cw.get("temperature") * 9/5) + 32, 2),
        "wind": cw.get("windspeed"),
        "code": cw.get("weathercode"),
    }