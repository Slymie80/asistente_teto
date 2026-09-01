
def interpretar_comando(texto:str) -> dict:
    """
    Interpreta un comando de texto y devuelve un diccionario con la intención, acción, parámetros y respuesta de texto.

    Args:
        texto (str): El comando de texto a interpretar.

    Returns:
        dict: Un diccionario con la intención, acción, parámetros y respuesta de texto.
    """
    if "hora" in texto.lower().strip():
        return {
            "intencion": "consultar_hora",
            "accion": "consultar_hora",
            "parametros": {},
            "respuesta_texto": "aqui tienes la hora "
        }
    if "hola" in texto.lower().strip():
        return {
            "intencion": "saludo",
            "accion": "saludar",
            "parametros": {},
            "respuesta_texto": "Hola, ¿cómo estás?"
        }
    if "abrir" in texto.lower().strip() or "abre" in texto.lower().strip():
        aplicacion = texto.lower().strip().split(" ")[-1]
        return {
            "intencion": "abrir_aplicacion",
            "accion": "abrir_aplicacion",
            "parametros": {"aplicacion": aplicacion},
            "respuesta_texto": f"Abriendo {aplicacion}..."
        }
    else:
        return {
            "intencion": "desconocida",
            "accion": "no_reconocida",
            "parametros": {},
            "respuesta_texto": "Lo siento, no entendí el comando."
        }
    