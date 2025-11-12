from fastapi import Request, HTTPException
import time

IP_REQUESTS = {}
LIMIT = 10
WINDOW = 60

async def rate_limiter(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    if ip not in IP_REQUESTS:
        IP_REQUESTS[ip] = []

    IP_REQUESTS[ip] = [t for t in IP_REQUESTS[ip] if now - t < WINDOW]

    if len(IP_REQUESTS[ip]) >= LIMIT:
        raise HTTPException(status_code=429, detail="Demasiadas solicitudes. Intenta más tarde.")

    IP_REQUESTS[ip].append(now)
    return await call_next(request)