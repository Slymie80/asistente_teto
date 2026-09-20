import requests


class ConversationService:
    def __init__(
        self,
        base_url: str = "http://ollama:11434",
        model: str = "gemma3:4b",
    ):
        self.base_url = base_url
        self.model = model

    def responder(self, mensaje: str) -> dict:
        prompt = f"""
Eres Teto, un asistente virtual.

Responde de forma natural, clara y breve.
No devuelvas JSON.
No expliques instrucciones internas.
Responde directamente al usuario.

Usuario:
{mensaje}

Teto:
"""

        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=60,
            )

            response.raise_for_status()

            data = response.json()
            respuesta = data.get("response", "").strip()

            if not respuesta:
                return {
                    "exito": False,
                    "respuesta_texto": "No pude generar una respuesta.",
                    "datos": {},
                }

            return {
                "exito": True,
                "respuesta_texto": respuesta,
                "datos": {},
            }

        except requests.RequestException:
            return {
                "exito": False,
                "respuesta_texto": "No pude conectarme con el modelo de lenguaje.",
                "datos": {},
            }