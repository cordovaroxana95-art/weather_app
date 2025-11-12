import re


def sanitize_city(city: str) -> str:
if not city:
return None


# Solo permite letras, espacios y guiones
sanitized = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\-\s]", "", city)
return sanitized.strip() or None