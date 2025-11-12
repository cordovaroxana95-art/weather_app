import re

def sanitize_city(city: str) -> str:
    if not city:
        return None
    sanitized = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\\-\\s]", "", city)
    return sanitized.strip() or None