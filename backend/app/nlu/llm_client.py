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

    def _crear_prompt(self,texto:str):
        return f"""
Eres el intérprete de comandos de un asistente virtual llamado Teto.

Convierte el mensaje del usuario en un comando estructurado.

Acciones disponibles:

- abrir_aplicacion
- cerrar_aplicacion
- consultar_hora
- buscar_web
- responder
- ninguna

Devuelve únicamente JSON.

Formato:

{{
    "intencion": "nombre_intencion",
    "accion": "nombre_accion",
    "parametros": {{}}
}}

Usuario:
{texto}

Respuesta:
"""
