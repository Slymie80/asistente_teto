from app.nlu.intents import ACCIONES_PERMITIDAS
from app.nlu.llm_client import LLMClient

class IntentParser:
    def __init__(self):
        self.llm = LLMClient()

    def interpretar(self,texto:str) -> dict:

        texto =texto.lower().strip()

        if not texto:
            return self._response_desconocida()

        resultado = self.llm.interpretar_por_llm(texto)

        if resultado.get("accion") not in ACCIONES_PERMITIDAS:
            return self._response_desconocida() 

        return resultado

    def _response_desconocida(self):
        return {
            "intencion": "desconocida",
            "accion": "ninguna",
            "parametros": {},
        }

        


    