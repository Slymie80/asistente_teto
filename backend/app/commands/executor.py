from app.commands.system import SystemCommands


class CommandExecutor:
    def __init__(self):
        self.system = SystemCommands()
        
        # definir un diccionario de acciones permitidas y sus correspondientes métodos
        self._handlers = {
            "consultar_hora": self.system.consultar_hora,
        }

    def ejecutar(self, comando: dict) -> dict:
        """ejecuta un comando basado en la acción y parámetros proporcionados.

        Args:
            comando (dict): Un diccionario que contiene la acción a ejecutar y los parámetros necesarios.

        Returns:
            dict: Un diccionario que indica si la ejecución fue exitosa, un mensaje de respuesta y cualquier dato adicional relevante.
        """

        accion = comando.get("accion")
        parametros = comando.get("parametros", {})

        # Validación de la acción
        handler = self._handlers.get(accion)


        if handler is None:
            return {
                "exito": False,
                "respuesta_texto": "Todavía no puedo ejecutar esa acción.",
                "datos": {
                    "accion": accion,
                    "parametros": parametros,
                },
            }

        return handler(**parametros)