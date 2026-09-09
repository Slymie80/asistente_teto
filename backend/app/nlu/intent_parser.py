from app.nlu.intents import ACCIONES_PERMITIDAS
from app.nlu.llm_client import LLMClient

class IntentParser:
    def __init__(self):
        self.llm = LLMClient()

    def interpretar(self,texto:str) -> dict:

        texto =texto.lower().strip()

        if not texto:
            return self._response_desconocida()
        try:
            resultado = self._interpretar_con_llm(texto)
        except Exception:
            return self._response_desconocida()

        if not isinstance(resultado, dict):
            return self._response_desconocida()

        intencion = resultado.get("intencion")
        accion = resultado.get("accion")
        parametros = resultado.get("parametros")

        if not isinstance(intencion, str) or not isinstance(accion, str) or not isinstance(parametros, dict):
            return self._response_desconocida()

        if accion not in ACCIONES_PERMITIDAS:
            return self._response_desconocida()

        if not isinstance(parametros, dict):
            return self._response_desconocida()

        return {
            "intencion": intencion,
            "accion": accion,
            "parametros": parametros,
            }

    def _response_desconocida(self):
        return {
            "intencion": "desconocida",
            "accion": "ninguna",
            "parametros": {},
        }

        


    