import os
import requests
import json

class LLMClient:
    def __init__(self):
        self.api_url = os.getenv(
            "OLLAMA_API_URL",
            "http://ollama:11434"
            )
        
        self.model = os.getenv(
            "OLLAMA_MODEL",
            "gemma3:1b"
        )
        self.timeout = 60

    def interpretar_por_llm (self,texto: str) -> dict:

        prompt = self._crear_prompt(texto)

        payload = {
            "model": self.model,
            "prompt":prompt,
            "stream": False,
            "format": "json"
        }

        response = requests.post(
            f"{self.api_url}/api/generate",
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()
        datos = response.json()

        return json.loads(datos["response"])

    def _crear_prompt(self, texto: str) -> str:
        return f"""
    Eres el módulo NLU de un asistente virtual.

    Tu única tarea es convertir el mensaje del usuario a JSON estructurado.

    REGLAS OBLIGATORIAS:

    1. Devuelve SOLO JSON válido.
    2. Usa EXACTAMENTE estas claves:
    - "intencion"
    - "accion"
    - "parametros"
    3. Nunca cambies el nombre de las claves.
    4. "accion" solo puede ser uno de estos valores:
    - "abrir_aplicacion"
    - "cerrar_aplicacion"
    - "consultar_hora"
    - "buscar_web"
    - "responder"
    - "ninguna"
    5. Si el usuario pide buscar, investigar, consultar información o encontrar algo en Internet:
    "accion" debe ser "buscar_web".
    6. Si pide la hora:
    "accion" debe ser "consultar_hora".
    7. Si pide abrir una aplicación:
    "accion" debe ser "abrir_aplicacion".
    8. Si pide cerrar una aplicación:
    "accion" debe ser "cerrar_aplicacion".
    9. Si es conversación normal:
    "accion" debe ser "responder".
    10. Si no puedes determinar la acción:
        "accion" debe ser "ninguna".

    EJEMPLOS:

    Usuario:
    abre spotify

    Respuesta:
    {{
    "intencion": "abrir_aplicacion",
    "accion": "abrir_aplicacion",
    "parametros": {{
        "aplicacion": "spotify"
    }}
    }}

    Usuario:
    qué hora es

    Respuesta:
    {{
    "intencion": "consultar_hora",
    "accion": "consultar_hora",
    "parametros": {{}}
    }}

    Usuario:
    busca información sobre Python

    Respuesta:
    {{
    "intencion": "buscar_web",
    "accion": "buscar_web",
    "parametros": {{
        "consulta": "Python"
    }}
    }}

    Usuario:
    {texto}

    Respuesta:
    """

