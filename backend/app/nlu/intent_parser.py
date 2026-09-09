
def interpretar_comando(texto:str) -> dict:
    """
    convierte un comando de texto en una intención, acción, parámetros y respuesta de texto. 

    """

    texto =texto.lower().strip()

    if not texto:
        return {
            "intencion": "desconocida",
            "accion": "ninguna",
            "parametros": {},
        }

    # luego se implementara llamada al llm

    return {
        "intencion":"desconocida",
        "accion":"ninguna",
        "parametros": {
            "texto_original": texto
        },
    }
    
    


    