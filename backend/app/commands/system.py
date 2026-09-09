from datatime import datetime

class SystemCommands:
    def consultar_hora(self) -> dict:
        ahora = datetime.now()
        return {
            "exito": True,
            "respuesta_texto": f"Son las {ahora.strftime('%H:%M')}",
            "datos": {
                "hora": ahora.strftime("%H:%M")
            },
        }
