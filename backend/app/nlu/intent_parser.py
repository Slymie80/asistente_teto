from app.nlu.intents import ACCIONES_PERMITIDAS
from app.nlu.llm_client import LLMClient
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

    resultado = {
        "intencion":"desconocida",
        "accion":"ninguna",
        "parametros": {},
    }

    if resultado["accion"] not in ACCIONES_PERMITIDAS:
        resultado["accion"] = "ninguna"

    return resultado

    


    